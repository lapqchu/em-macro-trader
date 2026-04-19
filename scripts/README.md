# EM Macro Trader — Reuters/LSEG Data Scripts

## Setup

1. Install one of the LSEG Python libraries on your work machine:
   ```bash
   pip install lseg-data          # newest (recommended)
   # OR: pip install refinitiv-data
   # OR: pip install eikon
   ```

2. Make sure Reuters Workspace is running (the scripts connect via the desktop session).

3. For eikon users: set your app key:
   ```bash
   export EIKON_APP_KEY=your_key_here
   ```

## Scripts

### `rates_trade.py` — Rate Trade Evaluator
Pull everything needed to evaluate a specific EM rates trade.

```bash
python rates_trade.py TH 5y             # Thailand 5Y IRS
python rates_trade.py BR 2y --hist      # Brazil 2Y with 1Y history
python rates_trade.py MX 10y -o mx.json # Mexico 10Y, save to file
```

**Output includes:**
- Target IRS level + full curve + slopes (2s5s, 2s10s)
- Local macro: policy rate, CPI, core CPI, GDP, current account, CDS
- Derived: real policy rate, 1Y-vs-policy turn signal
- FX spot
- Global regime: DXY, UST, HY OAS, VIX, commodities
- China: CNY, CNH, 10Y CGB
- Auto-generated Willer framework flags

### `macro_dashboard.py` — Global Macro Dashboard
Pull the global regime data that drives 65% of EM returns.

```bash
python macro_dashboard.py              # Snapshot
python macro_dashboard.py --hist       # With 3M history
python macro_dashboard.py -o dash.json # Save to file
```

**Output includes:**
- USD: DXY, EUR/USD, USD/JPY
- US rates: Fed funds, 2Y, 5Y, 10Y, 30Y + curve slopes
- Risk: VIX, US HY OAS, S&P 500
- Commodities: Brent, WTI, Gold, Copper
- China: USD/CNY, USD/CNH, CNY-CNH basis, 10Y CGB, PMI
- Auto-generated regime flags

### `country_snapshot.py` — Country Comparison
Quick snapshot for one or many countries.

```bash
python country_snapshot.py TH           # Single country
python country_snapshot.py TH BR MX ZA  # Multiple countries
python country_snapshot.py ALL          # All 13 countries
python country_snapshot.py ALL -o em.json
```

**Output includes:**
- All instrument levels per country
- Derived: real rate, 1Y-vs-policy, curve slopes
- Comparison table for quick cross-country scanning

## How to Use with Claude

1. Run the relevant script on your work machine
2. Copy the JSON output
3. Paste it into the conversation with your trade idea
4. Example: "Receive Thailand 5Y IRS — here's the data: [paste JSON]"

The skill will automatically parse the JSON and apply the Willer framework checklists.

## Customizing RICs

If any RIC doesn't work on your terminal, edit `config.py → COUNTRY_PROFILES`.
The RICs are common patterns but may vary by your Reuters subscription.

## Available Countries

| Code | Country      | Region | Currency |
|------|-------------|--------|----------|
| TH   | Thailand    | Asia   | THB      |
| BR   | Brazil      | Latam  | BRL      |
| MX   | Mexico      | Latam  | MXN      |
| ZA   | South Africa| CEEMEA | ZAR      |
| TR   | Turkey      | CEEMEA | TRY      |
| IN   | India       | Asia   | INR      |
| ID   | Indonesia   | Asia   | IDR      |
| PL   | Poland      | CEEMEA | PLN      |
| HU   | Hungary     | CEEMEA | HUF      |
| CL   | Chile       | Latam  | CLP      |
| CO   | Colombia    | Latam  | COP      |
| KR   | South Korea | Asia   | KRW      |
| MY   | Malaysia    | Asia   | MYR      |

To add a country: add a new entry to `COUNTRY_PROFILES` in `config.py`.
