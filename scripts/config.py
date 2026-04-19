"""
EM Macro Trader — Reuters/LSEG Data Configuration
==================================================
Central configuration for all data pull scripts.
Contains RIC mappings, field definitions, and country profiles.

Setup:
  pip install lseg-data   (or: pip install refinitiv-data / pip install eikon)

Authentication:
  The scripts auto-detect which library is available and attempt to connect.
  - lseg.data / refinitiv.data: Opens a session via Workspace (must be running)
  - eikon: Uses app_key (set EIKON_APP_KEY env variable or edit below)

Usage:
  Import this module from any script:
    from config import connect, COUNTRY_PROFILES, GLOBAL_RICS
"""

import os
import json
import sys
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Library auto-detection and connection
# ---------------------------------------------------------------------------

_session = None

def connect():
    """Connect to LSEG/Refinitiv. Returns the library module."""
    global _session

    # Try lseg.data first (newest)
    try:
        import lseg.data as ld
        ld.open_session()
        _session = ld
        print("[OK] Connected via lseg.data")
        return ld
    except ImportError:
        pass
    except Exception as e:
        print(f"[WARN] lseg.data found but connection failed: {e}")

    # Try refinitiv.data
    try:
        import refinitiv.data as rd
        rd.open_session()
        _session = rd
        print("[OK] Connected via refinitiv.data")
        return rd
    except ImportError:
        pass
    except Exception as e:
        print(f"[WARN] refinitiv.data found but connection failed: {e}")

    # Try eikon
    try:
        import eikon as ek
        app_key = os.environ.get("EIKON_APP_KEY", "YOUR_APP_KEY_HERE")
        ek.set_app_key(app_key)
        _session = ek
        print("[OK] Connected via eikon")
        return ek
    except ImportError:
        pass
    except Exception as e:
        print(f"[WARN] eikon found but connection failed: {e}")

    print("[ERROR] No LSEG/Refinitiv library available.")
    print("Install one of: pip install lseg-data / refinitiv-data / eikon")
    sys.exit(1)


def get_lib():
    """Return the connected library module."""
    if _session is None:
        return connect()
    return _session


def detect_lib_type():
    """Return 'lseg', 'refinitiv', or 'eikon'."""
    lib = get_lib()
    name = lib.__name__
    if "lseg" in name:
        return "lseg"
    elif "refinitiv" in name:
        return "refinitiv"
    else:
        return "eikon"


# ---------------------------------------------------------------------------
# RIC Mappings — Global Macro Indicators
# ---------------------------------------------------------------------------

GLOBAL_RICS = {
    # US rates
    "us_2y":        "US2YT=RR",
    "us_5y":        "US5YT=RR",
    "us_10y":       "US10YT=RR",
    "us_30y":       "US30YT=RR",
    "fed_funds":    "USDONFSR=X",

    # DXY and major FX
    "dxy":          "DXY",
    "eurusd":       "EUR=",
    "usdjpy":       "JPY=",

    # Risk indicators
    "vix":          ".VIX",
    "us_hy_oas":    ".MERH0A0",      # ICE BofA US HY OAS
    "spx":          ".SPX",

    # Commodities
    "brent":        "LCOc1",
    "wti":          "CLc1",
    "gold":         "XAU=",
    "copper":       "HGc1",

    # China
    "usdcny":       "CNY=",
    "usdcnh":       "CNH=",
    "china_10y":    "CN10YT=RR",
    "china_pmi":    "CNCPMINDX",
}


# ---------------------------------------------------------------------------
# Country Profiles — EM universe
# ---------------------------------------------------------------------------
# Each profile contains RICs for the instruments the skill needs.
# Adjust RICs based on your Reuters terminal's available instruments.
# IRS RICs vary by provider — these are common patterns; verify on your terminal.

COUNTRY_PROFILES = {
    "TH": {
        "name": "Thailand",
        "currency": "THB",
        "fx_ric": "THB=",
        "policy_rate_ric": "THBKP=ECI",       # BoT policy rate
        "cpi_ric": "THCPIY%",                  # CPI YoY
        "core_cpi_ric": "THCCPIY%",
        "gdp_ric": "THGDPY%",
        "ca_ric": "THCABAL",                   # Current account balance
        "irs_rics": {
            "1y": "THBIRS1Y=",
            "2y": "THBIRS2Y=",
            "3y": "THBIRS3Y=",
            "5y": "THBIRS5Y=",
            "7y": "THBIRS7Y=",
            "10y": "THBIRS10Y=",
        },
        "cds_ric": "THGV5YUSAC=R",
        "bond_10y_ric": "TH10YT=RR",
        "region": "Asia",
        "commodity_exposure": "net_importer",   # energy importer
        "fx_regime": "managed_float",
        "day_count": "ACT/365",
    },
    "BR": {
        "name": "Brazil",
        "currency": "BRL",
        "fx_ric": "BRL=",
        "policy_rate_ric": "BRSELIC=ECI",
        "cpi_ric": "BRCPIY%",
        "core_cpi_ric": "BRCCPIY%",
        "gdp_ric": "BRGDPY%",
        "ca_ric": "BRCABAL",
        "irs_rics": {
            "1y": "0#BRIRS1Y=",
            "2y": "BRIRS2Y=",
            "3y": "BRIRS3Y=",
            "5y": "BRIRS5Y=",
            "10y": "BRIRS10Y=",
        },
        "cds_ric": "BRGV5YUSAC=R",
        "bond_10y_ric": "BR10YT=RR",
        "region": "Latam",
        "commodity_exposure": "net_exporter",
        "fx_regime": "float",
        "day_count": "BUS/252",
    },
    "MX": {
        "name": "Mexico",
        "currency": "MXN",
        "fx_ric": "MXN=",
        "policy_rate_ric": "MXBRATE=ECI",
        "cpi_ric": "MXCPIY%",
        "core_cpi_ric": "MXCCPIY%",
        "gdp_ric": "MXGDPY%",
        "ca_ric": "MXCABAL",
        "irs_rics": {
            "1y": "MXNIRS1Y=",
            "2y": "MXNIRS2Y=",
            "3y": "MXNIRS3Y=",
            "5y": "MXNIRS5Y=",
            "10y": "MXNIRS10Y=",
        },
        "cds_ric": "MXGV5YUSAC=R",
        "bond_10y_ric": "MX10YT=RR",
        "region": "Latam",
        "commodity_exposure": "net_exporter",
        "fx_regime": "float",
        "day_count": "ACT/360",
    },
    "ZA": {
        "name": "South Africa",
        "currency": "ZAR",
        "fx_ric": "ZAR=",
        "policy_rate_ric": "ZASARATE=ECI",
        "cpi_ric": "ZACPIY%",
        "core_cpi_ric": "ZACCPIY%",
        "gdp_ric": "ZAGDPY%",
        "ca_ric": "ZACABAL",
        "irs_rics": {
            "2y": "ZARIRS2Y=",
            "5y": "ZARIRS5Y=",
            "10y": "ZARIRS10Y=",
        },
        "cds_ric": "ZAGV5YUSAC=R",
        "bond_10y_ric": "ZA10YT=RR",
        "region": "CEEMEA",
        "commodity_exposure": "net_exporter",
        "fx_regime": "float",
        "day_count": "ACT/365",
    },
    "TR": {
        "name": "Turkey",
        "currency": "TRY",
        "fx_ric": "TRY=",
        "policy_rate_ric": "TRINT=ECI",
        "cpi_ric": "TRCPIY%",
        "core_cpi_ric": "TRCCPIY%",
        "gdp_ric": "TRGDPY%",
        "ca_ric": "TRCABAL",
        "irs_rics": {
            "1y": "TRYIRS1Y=",
            "2y": "TRYIRS2Y=",
            "5y": "TRYIRS5Y=",
            "10y": "TRYIRS10Y=",
        },
        "cds_ric": "TRGV5YUSAC=R",
        "bond_10y_ric": "TR10YT=RR",
        "region": "CEEMEA",
        "commodity_exposure": "net_importer",
        "fx_regime": "managed_float",
        "day_count": "ACT/360",
    },
    "IN": {
        "name": "India",
        "currency": "INR",
        "fx_ric": "INR=",
        "policy_rate_ric": "INREPO=ECI",
        "cpi_ric": "INCPIY%",
        "core_cpi_ric": "INCCPIY%",
        "gdp_ric": "INGDPY%",
        "ca_ric": "INCABAL",
        "irs_rics": {
            "1y": "INRIRS1Y=",
            "2y": "INRIRS2Y=",
            "5y": "INRIRS5Y=",
            "10y": "INRIRS10Y=",
        },
        "cds_ric": "INGV5YUSAC=R",
        "bond_10y_ric": "IN10YT=RR",
        "region": "Asia",
        "commodity_exposure": "net_importer",
        "fx_regime": "managed_float",
        "day_count": "ACT/365",
    },
    "ID": {
        "name": "Indonesia",
        "currency": "IDR",
        "fx_ric": "IDR=",
        "policy_rate_ric": "IDBIRATE=ECI",
        "cpi_ric": "IDCPIY%",
        "core_cpi_ric": "IDCCPIY%",
        "gdp_ric": "IDGDPY%",
        "ca_ric": "IDCABAL",
        "irs_rics": {
            "1y": "IDRIRS1Y=",
            "2y": "IDRIRS2Y=",
            "5y": "IDRIRS5Y=",
            "10y": "IDRIRS10Y=",
        },
        "cds_ric": "IDGV5YUSAC=R",
        "bond_10y_ric": "ID10YT=RR",
        "region": "Asia",
        "commodity_exposure": "net_exporter",
        "fx_regime": "managed_float",
        "day_count": "ACT/360",
    },
    "PL": {
        "name": "Poland",
        "currency": "PLN",
        "fx_ric": "PLN=",
        "policy_rate_ric": "PLNBRATE=ECI",
        "cpi_ric": "PLCPIY%",
        "core_cpi_ric": "PLCCPIY%",
        "gdp_ric": "PLGDPY%",
        "ca_ric": "PLCABAL",
        "irs_rics": {
            "2y": "PLNIRS2Y=",
            "5y": "PLNIRS5Y=",
            "10y": "PLNIRS10Y=",
        },
        "cds_ric": "PLGV5YUSAC=R",
        "bond_10y_ric": "PL10YT=RR",
        "region": "CEEMEA",
        "commodity_exposure": "net_importer",
        "fx_regime": "float",
        "day_count": "ACT/365",
    },
    "HU": {
        "name": "Hungary",
        "currency": "HUF",
        "fx_ric": "HUF=",
        "policy_rate_ric": "HUNBRATE=ECI",
        "cpi_ric": "HUCPIY%",
        "core_cpi_ric": "HUCCPIY%",
        "gdp_ric": "HUGDPY%",
        "ca_ric": "HUCABAL",
        "irs_rics": {
            "2y": "HUFIRS2Y=",
            "5y": "HUFIRS5Y=",
            "10y": "HUFIRS10Y=",
        },
        "cds_ric": "HUGV5YUSAC=R",
        "bond_10y_ric": "HU10YT=RR",
        "region": "CEEMEA",
        "commodity_exposure": "net_importer",
        "fx_regime": "float",
        "day_count": "ACT/360",
    },
    "CL": {
        "name": "Chile",
        "currency": "CLP",
        "fx_ric": "CLP=",
        "policy_rate_ric": "CLBRATE=ECI",
        "cpi_ric": "CLCPIY%",
        "gdp_ric": "CLGDPY%",
        "ca_ric": "CLCABAL",
        "irs_rics": {
            "2y": "CLPIRS2Y=",
            "5y": "CLPIRS5Y=",
            "10y": "CLPIRS10Y=",
        },
        "cds_ric": "CLGV5YUSAC=R",
        "region": "Latam",
        "commodity_exposure": "net_exporter",
        "fx_regime": "float",
        "day_count": "ACT/360",
    },
    "CO": {
        "name": "Colombia",
        "currency": "COP",
        "fx_ric": "COP=",
        "policy_rate_ric": "COBRATE=ECI",
        "cpi_ric": "COCPIY%",
        "gdp_ric": "COGDPY%",
        "ca_ric": "COCABAL",
        "irs_rics": {
            "1y": "COPIRS1Y=",
            "2y": "COPIRS2Y=",
            "5y": "COPIRS5Y=",
            "10y": "COPIRS10Y=",
        },
        "cds_ric": "COGV5YUSAC=R",
        "region": "Latam",
        "commodity_exposure": "net_exporter",
        "fx_regime": "float",
        "day_count": "ACT/360",
    },
    "KR": {
        "name": "South Korea",
        "currency": "KRW",
        "fx_ric": "KRW=",
        "policy_rate_ric": "KRBRATE=ECI",
        "cpi_ric": "KRCPIY%",
        "core_cpi_ric": "KRCCPIY%",
        "gdp_ric": "KRGDPY%",
        "ca_ric": "KRCABAL",
        "irs_rics": {
            "1y": "KRWIRS1Y=",
            "2y": "KRWIRS2Y=",
            "3y": "KRWIRS3Y=",
            "5y": "KRWIRS5Y=",
            "10y": "KRWIRS10Y=",
        },
        "cds_ric": "KRGV5YUSAC=R",
        "bond_10y_ric": "KR10YT=RR",
        "region": "Asia",
        "commodity_exposure": "net_importer",
        "fx_regime": "managed_float",
        "day_count": "ACT/365",
    },
    "MY": {
        "name": "Malaysia",
        "currency": "MYR",
        "fx_ric": "MYR=",
        "policy_rate_ric": "MYBKP=ECI",
        "cpi_ric": "MYCPIY%",
        "gdp_ric": "MYGDPY%",
        "ca_ric": "MYCABAL",
        "irs_rics": {
            "2y": "MYRIRS2Y=",
            "5y": "MYRIRS5Y=",
            "10y": "MYRIRS10Y=",
        },
        "cds_ric": "MYGV5YUSAC=R",
        "region": "Asia",
        "commodity_exposure": "net_exporter",
        "fx_regime": "managed_float",
        "day_count": "ACT/365",
    },
}


# ---------------------------------------------------------------------------
# Data fetch helpers (shared across scripts)
# ---------------------------------------------------------------------------

def safe_get_data(rics, fields=None):
    """Fetch snapshot data for one or more RICs, handling errors gracefully."""
    lib = get_lib()
    lib_type = detect_lib_type()
    results = {}
    if isinstance(rics, str):
        rics = [rics]
    for ric in rics:
        try:
            if lib_type == "eikon":
                if fields:
                    df, _ = lib.get_data(ric, fields)
                else:
                    df, _ = lib.get_data(ric, ["CF_LAST", "CF_BID", "CF_ASK"])
                if df is not None and not df.empty:
                    results[ric] = df.iloc[0].to_dict()
            else:
                if fields:
                    df = lib.get_data(ric, fields)
                else:
                    df = lib.get_data(ric, ["CF_LAST", "CF_BID", "CF_ASK"])
                if df is not None and not df.empty:
                    results[ric] = df.iloc[0].to_dict()
        except Exception as e:
            results[ric] = {"error": str(e)}
    return results


def safe_get_timeseries(ric, start, end, interval="daily"):
    """Fetch time series for a single RIC, handling errors gracefully."""
    lib = get_lib()
    lib_type = detect_lib_type()
    try:
        if lib_type == "eikon":
            df = lib.get_timeseries(ric, start_date=start, end_date=end,
                                     interval=interval, fields=["CLOSE"])
        else:
            df = lib.get_history(ric, start=start, end=end, interval=interval)
        if df is not None and not df.empty:
            records = []
            for idx, row in df.iterrows():
                records.append({
                    "date": str(idx.date()) if hasattr(idx, 'date') else str(idx),
                    "value": float(row.iloc[0]) if len(row) > 0 else None
                })
            return records
    except Exception as e:
        return [{"error": str(e)}]
    return []


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def output_json(data: dict, filename: str = None):
    """Print JSON to stdout. Optionally save to file."""
    output = json.dumps(data, indent=2, default=str)
    print(output)
    if filename:
        with open(filename, "w") as f:
            f.write(output)
        print(f"\n[Saved to {filename}]")


def today_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M")
