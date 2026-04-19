"""
EM Macro Trader — Rates Trade Evaluator
========================================
Pulls all data needed to evaluate an EM rates trade idea using
the Willer framework (rate cycle checklist + global macro regime).

Usage:
  python rates_trade.py TH 5y          # Thailand 5Y IRS
  python rates_trade.py BR 2y          # Brazil 2Y IRS
  python rates_trade.py MX 10y         # Mexico 10Y IRS
  python rates_trade.py TH 5y --hist   # Include 1Y historical time series
  python rates_trade.py TH 5y -o out.json  # Save to file

Output:
  JSON blob ready to paste into the EM Macro Trader skill conversation.
  The skill will parse this and apply the Willer frameworks automatically.

RIC Note:
  If any RIC fails, the script logs a warning and continues.
  You can fix RICs in config.py → COUNTRY_PROFILES for your terminal.
"""

import argparse
import sys
from datetime import datetime, timedelta

from config import (
    connect, get_lib, detect_lib_type,
    COUNTRY_PROFILES, GLOBAL_RICS, output_json, today_str,
    safe_get_data, safe_get_timeseries
)


def pull_country_rates_data(country_code, tenor, include_hist=False):
    """Pull all data needed for a rates trade evaluation."""
    profile = COUNTRY_PROFILES.get(country_code.upper())

    if not profile:
        print(f"[ERROR] Country '{country_code}' not found. Available: {list(COUNTRY_PROFILES.keys())}")
        sys.exit(1)

    tenor_key = tenor.lower().replace("y", "y").replace("yr", "y")
    target_ric = profile["irs_rics"].get(tenor_key)
    if not target_ric:
        avail = list(profile["irs_rics"].keys())
        print(f"[ERROR] Tenor '{tenor}' not found for {profile['name']}. Available: {avail}")
        sys.exit(1)

    result = {
        "meta": {
            "script": "rates_trade.py",
            "timestamp": today_str(),
            "country": profile["name"],
            "country_code": country_code.upper(),
            "currency": profile["currency"],
            "target_instrument": f"{profile['currency']} {tenor_key.upper()} IRS",
            "target_ric": target_ric,
            "day_count": profile.get("day_count", "unknown"),
            "region": profile["region"],
            "commodity_exposure": profile["commodity_exposure"],
            "fx_regime": profile["fx_regime"],
        },
        "target_instrument": {},
        "irs_curve": {},
        "macro_local": {},
        "fx": {},
        "global_regime": {},
        "risk_indicators": {},
        "china": {},
    }

    print(f"[Pulling data for {profile['name']} {tenor_key.upper()} IRS...]")

    # --- Target instrument ---
    print("  → Target IRS level...")
    data = safe_get_data(target_ric)
    result["target_instrument"] = data.get(target_ric, {})

    # --- Full IRS curve ---
    print("  → IRS curve...")
    curve_rics = list(profile["irs_rics"].values())
    curve_data = safe_get_data(curve_rics)
    for tenor_label, ric in profile["irs_rics"].items():
        val = curve_data.get(ric, {})
        last = val.get("CF_LAST") or val.get("CF_BID")
        result["irs_curve"][tenor_label] = {
            "ric": ric,
            "level": last,
            "raw": val
        }

    # --- Compute curve slopes ---
    try:
        curve_levels = {k: v["level"] for k, v in result["irs_curve"].items() if v["level"]}
        if "2y" in curve_levels and "5y" in curve_levels:
            result["irs_curve"]["2s5s_slope"] = round(curve_levels["5y"] - curve_levels["2y"], 2)
        if "2y" in curve_levels and "10y" in curve_levels:
            result["irs_curve"]["2s10s_slope"] = round(curve_levels["10y"] - curve_levels["2y"], 2)
        if "1y" in curve_levels:
            result["irs_curve"]["1y_level"] = curve_levels["1y"]
    except:
        pass

    # --- Local macro ---
    print("  → Local macro (policy rate, CPI, GDP, CA)...")
    macro_rics = {}
    for field in ["policy_rate_ric", "cpi_ric", "core_cpi_ric", "gdp_ric", "ca_ric", "cds_ric"]:
        if field in profile:
            macro_rics[field] = profile[field]

    macro_data = safe_get_data(list(macro_rics.values()))
    for field, ric in macro_rics.items():
        val = macro_data.get(ric, {})
        last = val.get("CF_LAST") or val.get("CF_BID")
        result["macro_local"][field.replace("_ric", "")] = {
            "ric": ric,
            "value": last,
            "raw": val
        }

    # --- Derived: real policy rate, 1Y vs policy rate ---
    try:
        policy = result["macro_local"].get("policy_rate", {}).get("value")
        cpi = result["macro_local"].get("cpi", {}).get("value")
        irs_1y = result["irs_curve"].get("1y", {}).get("level")

        if policy is not None and cpi is not None:
            result["macro_local"]["real_policy_rate"] = round(policy - cpi, 2)
        if irs_1y is not None and policy is not None:
            result["macro_local"]["1y_minus_policy"] = round(irs_1y - policy, 2)
            if irs_1y < policy:
                result["macro_local"]["turn_signal"] = "1Y BELOW policy rate → easing signal (Willer receive signal)"
            else:
                result["macro_local"]["turn_signal"] = "1Y ABOVE policy rate → no easing signal yet"
    except:
        pass

    # --- FX ---
    print("  → FX...")
    fx_ric = profile.get("fx_ric")
    if fx_ric:
        fx_data = safe_get_data(fx_ric)
        result["fx"] = fx_data.get(fx_ric, {})

    # --- Global macro regime ---
    print("  → Global regime (DXY, UST, HY, VIX, commodities)...")
    global_keys = ["dxy", "us_2y", "us_5y", "us_10y", "vix", "us_hy_oas", "spx", "brent", "copper"]
    global_ric_list = {k: GLOBAL_RICS[k] for k in global_keys if k in GLOBAL_RICS}
    global_data = safe_get_data(list(global_ric_list.values()))
    for key, ric in global_ric_list.items():
        val = global_data.get(ric, {})
        last = val.get("CF_LAST") or val.get("CF_BID")
        result["global_regime"][key] = {"ric": ric, "value": last}

    # --- China ---
    print("  → China...")
    china_keys = ["usdcny", "usdcnh", "china_10y"]
    china_ric_list = {k: GLOBAL_RICS[k] for k in china_keys if k in GLOBAL_RICS}
    china_data = safe_get_data(list(china_ric_list.values()))
    for key, ric in china_ric_list.items():
        val = china_data.get(ric, {})
        last = val.get("CF_LAST") or val.get("CF_BID")
        result["china"][key] = {"ric": ric, "value": last}

    # --- Historical time series (optional) ---
    if include_hist:
        print("  → Historical time series (1Y)...")
        end = datetime.now().strftime("%Y-%m-%d")
        start = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

        result["history"] = {}

        # Target IRS
        result["history"]["target_irs"] = safe_get_timeseries(target_ric, start, end)

        # Policy rate
        pr_ric = profile.get("policy_rate_ric")
        if pr_ric:
            result["history"]["policy_rate"] = safe_get_timeseries(pr_ric, start, end)

        # FX
        if fx_ric:
            result["history"]["fx"] = safe_get_timeseries(fx_ric, start, end)

        # CPI
        cpi_ric = profile.get("cpi_ric")
        if cpi_ric:
            result["history"]["cpi"] = safe_get_timeseries(cpi_ric, start, end)

    # --- Willer checklist status ---
    print("  → Generating Willer checklist flags...")
    result["willer_flags"] = generate_willer_flags(result)

    print(f"\n[Done — {profile['name']} {tenor_key.upper()} IRS data pull complete]\n")
    return result


def generate_willer_flags(data):
    """Auto-generate checklist flags from the data per Willer framework."""
    flags = {}

    # Turn signal: 1Y vs policy rate
    turn = data.get("macro_local", {}).get("turn_signal")
    if turn:
        flags["rate_cycle_turn_signal"] = turn

    # Real policy rate
    rpr = data.get("macro_local", {}).get("real_policy_rate")
    if rpr is not None:
        if rpr > 3.0:
            flags["real_rate_assessment"] = f"Real policy rate {rpr}% — elevated, supports receive thesis"
        elif rpr > 1.0:
            flags["real_rate_assessment"] = f"Real policy rate {rpr}% — moderate"
        else:
            flags["real_rate_assessment"] = f"Real policy rate {rpr}% — low, limited room for rally"

    # Curve shape
    slope_2s10s = data.get("irs_curve", {}).get("2s10s_slope")
    if slope_2s10s is not None:
        if slope_2s10s < 0:
            flags["curve_shape"] = f"2s10s inverted ({slope_2s10s}bp) — possible easing priced or stress"
        elif slope_2s10s > 100:
            flags["curve_shape"] = f"2s10s steep ({slope_2s10s}bp) — steepener may be preferred over outright"
        else:
            flags["curve_shape"] = f"2s10s at {slope_2s10s}bp — normal"

    # Commodity exposure vs oil
    exposure = data.get("meta", {}).get("commodity_exposure")
    brent = data.get("global_regime", {}).get("brent", {}).get("value")
    if exposure and brent:
        if exposure == "net_importer":
            flags["commodity_constraint"] = f"Net energy importer; Brent at {brent} — rising oil is a rates headwind (inflation pass-through)"
        else:
            flags["commodity_constraint"] = f"Net exporter; Brent at {brent} — rising oil strengthens FX, can paradoxically support receivers (Willer: commodity exporters benefit from rallies through FX)"

    # VIX / risk regime
    vix_val = data.get("global_regime", {}).get("vix", {}).get("value")
    if vix_val:
        if vix_val > 25:
            flags["risk_regime"] = f"VIX at {vix_val} — elevated; risk-off may constrain local CB"
        elif vix_val > 18:
            flags["risk_regime"] = f"VIX at {vix_val} — moderate"
        else:
            flags["risk_regime"] = f"VIX at {vix_val} — benign; supportive for EM rates"

    # CDS
    cds_val = data.get("macro_local", {}).get("cds", {}).get("value")
    if cds_val:
        if cds_val > 200:
            flags["credit_risk"] = f"5Y CDS at {cds_val}bp — elevated; credit component material for rates (Willer: >200bp CDS = credit drives rates)"
        elif cds_val > 100:
            flags["credit_risk"] = f"5Y CDS at {cds_val}bp — moderate"
        else:
            flags["credit_risk"] = f"5Y CDS at {cds_val}bp — low; minimal credit drag on rates"

    return flags


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EM Rates Trade Evaluator")
    parser.add_argument("country", help="Country code (TH, BR, MX, ZA, TR, IN, ID, PL, HU, CL, CO, KR, MY)")
    parser.add_argument("tenor", help="IRS tenor (1y, 2y, 3y, 5y, 7y, 10y)")
    parser.add_argument("--hist", action="store_true", help="Include 1Y historical time series")
    parser.add_argument("-o", "--output", help="Save JSON to file")

    args = parser.parse_args()

    lib = connect()
    data = pull_country_rates_data(args.country, args.tenor, include_hist=args.hist)
    output_json(data, args.output)
