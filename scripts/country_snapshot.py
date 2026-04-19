"""
EM Macro Trader — Country Snapshot
===================================
Quick single-country data pull: FX, rates curve, macro indicators.
Lighter than rates_trade.py — use for screening or comparing countries.

Usage:
  python country_snapshot.py TH          # Thailand snapshot
  python country_snapshot.py BR MX ZA    # Multiple countries
  python country_snapshot.py ALL         # All countries in config
  python country_snapshot.py TH -o th.json

Output:
  JSON with current levels for all instruments in the country profile.
"""

import argparse
import sys

from config import (
    connect, get_lib, detect_lib_type,
    COUNTRY_PROFILES, output_json, today_str,
    safe_get_data
)


def pull_country_snapshot(country_code):
    """Pull snapshot for a single country."""
    profile = COUNTRY_PROFILES.get(country_code.upper())

    if not profile:
        print(f"[ERROR] Country '{country_code}' not found. Available: {list(COUNTRY_PROFILES.keys())}")
        return None

    print(f"  → {profile['name']}...")

    # Collect all RICs for this country
    all_rics = {}

    # FX
    if "fx_ric" in profile:
        all_rics["fx"] = profile["fx_ric"]

    # IRS curve
    for tenor, ric in profile.get("irs_rics", {}).items():
        all_rics[f"irs_{tenor}"] = ric

    # Macro
    for field in ["policy_rate_ric", "cpi_ric", "core_cpi_ric", "gdp_ric", "ca_ric", "cds_ric"]:
        if field in profile:
            all_rics[field.replace("_ric", "")] = profile[field]

    # Bond
    if "bond_10y_ric" in profile:
        all_rics["bond_10y"] = profile["bond_10y_ric"]

    # Pull all at once
    data = safe_get_data(list(all_rics.values()))

    # Build result
    snapshot = {
        "country": profile["name"],
        "code": country_code.upper(),
        "currency": profile["currency"],
        "region": profile["region"],
        "commodity_exposure": profile["commodity_exposure"],
        "fx_regime": profile["fx_regime"],
        "levels": {},
    }

    for label, ric in all_rics.items():
        val = data.get(ric, {})
        last = val.get("CF_LAST") or val.get("CF_BID")
        snapshot["levels"][label] = {"ric": ric, "value": last}

    # Derived metrics
    try:
        pr = snapshot["levels"].get("policy_rate", {}).get("value")
        cpi = snapshot["levels"].get("cpi", {}).get("value")
        irs_1y = snapshot["levels"].get("irs_1y", {}).get("value")

        if pr is not None and cpi is not None:
            snapshot["real_policy_rate"] = round(pr - cpi, 2)
        if irs_1y is not None and pr is not None:
            snapshot["1y_vs_policy"] = round(irs_1y - pr, 2)

        # Curve slopes
        irs_2y = snapshot["levels"].get("irs_2y", {}).get("value")
        irs_5y = snapshot["levels"].get("irs_5y", {}).get("value")
        irs_10y = snapshot["levels"].get("irs_10y", {}).get("value")
        if irs_2y and irs_10y:
            snapshot["2s10s"] = round(irs_10y - irs_2y, 2)
        if irs_2y and irs_5y:
            snapshot["2s5s"] = round(irs_5y - irs_2y, 2)
    except:
        pass

    return snapshot


def pull_multi_snapshot(country_codes):
    """Pull snapshots for multiple countries."""
    result = {
        "meta": {
            "script": "country_snapshot.py",
            "timestamp": today_str(),
            "countries": country_codes,
        },
        "snapshots": {},
    }

    print(f"[Pulling snapshots for {len(country_codes)} countries...]")
    for code in country_codes:
        snap = pull_country_snapshot(code)
        if snap:
            result["snapshots"][code.upper()] = snap

    # Comparison table for quick scanning
    print("  → Building comparison table...")
    comparison = []
    for code, snap in result["snapshots"].items():
        row = {
            "country": snap["country"],
            "code": code,
            "fx": snap["levels"].get("fx", {}).get("value"),
            "policy_rate": snap["levels"].get("policy_rate", {}).get("value"),
            "cpi": snap["levels"].get("cpi", {}).get("value"),
            "real_rate": snap.get("real_policy_rate"),
            "1y_vs_policy": snap.get("1y_vs_policy"),
            "2s10s": snap.get("2s10s"),
            "cds": snap["levels"].get("cds", {}).get("value"),
        }
        comparison.append(row)

    result["comparison_table"] = comparison

    print(f"\n[Done — {len(country_codes)} country snapshots complete]\n")
    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EM Country Snapshot")
    parser.add_argument("countries", nargs="+",
                        help="Country codes (TH BR MX ...) or ALL for all countries")
    parser.add_argument("-o", "--output", help="Save JSON to file")
    args = parser.parse_args()

    lib = connect()

    if "ALL" in [c.upper() for c in args.countries]:
        codes = list(COUNTRY_PROFILES.keys())
    else:
        codes = [c.upper() for c in args.countries]

    data = pull_multi_snapshot(codes)
    output_json(data, args.output)
