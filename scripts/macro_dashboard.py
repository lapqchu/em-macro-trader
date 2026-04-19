"""
EM Macro Trader — Global Macro Dashboard
=========================================
Pulls the global macro regime data that drives 65% of EM returns
(per Willer framework). Run this before any trade evaluation to
understand the top-down environment.

Usage:
  python macro_dashboard.py             # Snapshot
  python macro_dashboard.py --hist      # Include 3M history for trend
  python macro_dashboard.py -o dash.json

Output:
  JSON blob with DXY, UST curve, US HY OAS, VIX, commodities, China,
  plus auto-generated regime flags.
"""

import argparse
from datetime import datetime, timedelta

from config import (
    connect, get_lib, detect_lib_type, GLOBAL_RICS, output_json, today_str,
    safe_get_data, safe_get_timeseries
)


def pull_macro_dashboard(include_hist=False):
    """Pull full global macro dashboard."""

    result = {
        "meta": {
            "script": "macro_dashboard.py",
            "timestamp": today_str(),
            "purpose": "Global macro regime assessment (Willer: 65% of EM returns)"
        },
        "usd": {},
        "us_rates": {},
        "us_curve": {},
        "risk": {},
        "commodities": {},
        "china": {},
        "regime_flags": {},
    }

    # --- USD ---
    print("[Pulling global macro dashboard...]")
    print("  → USD...")
    for key in ["dxy", "eurusd", "usdjpy"]:
        ric = GLOBAL_RICS.get(key)
        if ric:
            data = safe_get_data(ric)
            val = data.get(ric, {})
            result["usd"][key] = {"ric": ric, "value": val.get("CF_LAST") or val.get("CF_BID")}

    # --- US Rates ---
    print("  → US rates...")
    for key in ["fed_funds", "us_2y", "us_5y", "us_10y", "us_30y"]:
        ric = GLOBAL_RICS.get(key)
        if ric:
            data = safe_get_data(ric)
            val = data.get(ric, {})
            result["us_rates"][key] = {"ric": ric, "value": val.get("CF_LAST") or val.get("CF_BID")}

    # --- US Curve ---
    try:
        r2 = result["us_rates"].get("us_2y", {}).get("value")
        r10 = result["us_rates"].get("us_10y", {}).get("value")
        r30 = result["us_rates"].get("us_30y", {}).get("value")
        if r2 is not None and r10 is not None:
            result["us_curve"]["2s10s"] = round(r10 - r2, 2)
        if r10 is not None and r30 is not None:
            result["us_curve"]["10s30s"] = round(r30 - r10, 2)
        if r2 is not None and r30 is not None:
            result["us_curve"]["2s30s"] = round(r30 - r2, 2)
    except:
        pass

    # --- Risk ---
    print("  → Risk indicators...")
    for key in ["vix", "us_hy_oas", "spx"]:
        ric = GLOBAL_RICS.get(key)
        if ric:
            data = safe_get_data(ric)
            val = data.get(ric, {})
            result["risk"][key] = {"ric": ric, "value": val.get("CF_LAST") or val.get("CF_BID")}

    # --- Commodities ---
    print("  → Commodities...")
    for key in ["brent", "wti", "gold", "copper"]:
        ric = GLOBAL_RICS.get(key)
        if ric:
            data = safe_get_data(ric)
            val = data.get(ric, {})
            result["commodities"][key] = {"ric": ric, "value": val.get("CF_LAST") or val.get("CF_BID")}

    # --- China ---
    print("  → China...")
    for key in ["usdcny", "usdcnh", "china_10y", "china_pmi"]:
        ric = GLOBAL_RICS.get(key)
        if ric:
            data = safe_get_data(ric)
            val = data.get(ric, {})
            result["china"][key] = {"ric": ric, "value": val.get("CF_LAST") or val.get("CF_BID")}

    # --- CNY-CNH basis ---
    try:
        cny = result["china"].get("usdcny", {}).get("value")
        cnh = result["china"].get("usdcnh", {}).get("value")
        if cny and cnh:
            result["china"]["cny_cnh_basis"] = round(cnh - cny, 4)
    except:
        pass

    # --- History (optional) ---
    if include_hist:
        print("  → 3M historical trends...")
        end = datetime.now().strftime("%Y-%m-%d")
        start = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
        result["history"] = {}
        for key in ["dxy", "us_10y", "vix", "us_hy_oas", "brent"]:
            ric = GLOBAL_RICS.get(key)
            if ric:
                result["history"][key] = safe_get_timeseries(ric, start, end)

    # --- Regime flags ---
    print("  → Generating regime flags...")
    result["regime_flags"] = generate_regime_flags(result)

    print(f"\n[Done — Global macro dashboard complete]\n")
    return result


def generate_regime_flags(data):
    """Auto-assess the global regime per Willer hierarchy."""
    flags = {}

    # DXY direction
    dxy = data.get("usd", {}).get("dxy", {}).get("value")
    if dxy:
        flags["dxy"] = f"DXY at {dxy} — Willer: DXY is the dominant driver of EMFX (65% explained by global macro)"

    # US HY — most reliable EM leading indicator
    hy = data.get("risk", {}).get("us_hy_oas", {}).get("value")
    if hy:
        if hy > 500:
            flags["us_hy"] = f"US HY OAS at {hy}bp — WIDE; Willer: rising US HY worse than rising VIX for EM. Defensive posture."
        elif hy > 400:
            flags["us_hy"] = f"US HY OAS at {hy}bp — elevated; watching for further widening"
        elif hy > 300:
            flags["us_hy"] = f"US HY OAS at {hy}bp — normal range"
        else:
            flags["us_hy"] = f"US HY OAS at {hy}bp — tight; supportive for EM risk"

    # VIX
    vix = data.get("risk", {}).get("vix", {}).get("value")
    if vix:
        if vix > 30:
            flags["vix"] = f"VIX at {vix} — high; but Willer: avoiding EM rates during rising VIX does NOT add alpha"
        elif vix > 20:
            flags["vix"] = f"VIX at {vix} — moderate"
        else:
            flags["vix"] = f"VIX at {vix} — low; benign risk environment"

    # UST curve
    curve_2s10s = data.get("us_curve", {}).get("2s10s")
    if curve_2s10s is not None:
        if curve_2s10s < 0:
            flags["ust_curve"] = f"UST 2s10s at {curve_2s10s}bp — INVERTED; Willer: cut EM credit on disinversion if US-centric"
        elif curve_2s10s < 30:
            flags["ust_curve"] = f"UST 2s10s at {curve_2s10s}bp — flat; watch for inversion/disinversion"
        else:
            flags["ust_curve"] = f"UST 2s10s at {curve_2s10s}bp — normal"

    # UST sell-off check
    us10 = data.get("us_rates", {}).get("us_10y", {}).get("value")
    if us10:
        flags["ust_level"] = f"US 10Y at {us10}% — Willer: >100bp sell-off in 3 months is reliably EMFX negative"

    # Commodities — regional allocation signal
    brent = data.get("commodities", {}).get("brent", {}).get("value")
    if brent:
        flags["commodities"] = f"Brent at ${brent} — Willer: bullish commodities → overweight Latam over Asia"

    # China
    cny = data.get("china", {}).get("usdcny", {}).get("value")
    cnh = data.get("china", {}).get("usdcnh", {}).get("value")
    basis = data.get("china", {}).get("cny_cnh_basis")
    if cny and cnh:
        flags["china_fx"] = f"USD/CNY {cny}, USD/CNH {cnh}, basis {basis} — Willer: 12M CNH fwd >5% weaker than spot = extended shorts"

    return flags


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EM Global Macro Dashboard")
    parser.add_argument("--hist", action="store_true", help="Include 3M history")
    parser.add_argument("-o", "--output", help="Save JSON to file")
    args = parser.parse_args()

    lib = connect()
    data = pull_macro_dashboard(include_hist=args.hist)
    output_json(data, args.output)
