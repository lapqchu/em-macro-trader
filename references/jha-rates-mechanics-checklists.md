# Jha — Interest Rate Markets: Tradeable Checklists
# Structured for em-macro-trader skill integration

---

## Checklist 1: Carry Trade Evaluation

Use when evaluating any carry position — outright bonds, IRS receivers, ED strips, or EM local curves.

### Step 1: Compute Carry + Rolldown
- [ ] Calculate **carry in price terms**: coupon income − financing cost over holding period
- [ ] Convert to **carry in yield terms**: divide price carry by duration
- [ ] Calculate **rolldown**: yield at aged maturity (on static curve) minus current yield
- [ ] Combined breakeven = carry + rolldown. This is how much the curve can move against you
- [ ] **Cross-check via forwards**: carry + rolldown = forward rate at aged maturity − spot rate at aged maturity (current yield cancels out)
- [ ] Clarify whether you mean "carry" or "carry + rolldown" — market convention conflates them

### Step 2: Assess Carry-to-Risk Ratio
- [ ] Annualize carry (e.g., 3M carry × 4)
- [ ] Compute annualized yield vol: daily bp vol × √251
- [ ] **Carry-to-risk = annualized carry / annualized vol**
- [ ] Repeat using **stress-period vol**, not just recent vol — backward-looking risk measures are dangerous
- [ ] Compare across instruments: hedged carry trades (curves, butterflies) often have lower absolute carry but higher carry-to-risk

### Step 3: Crowding Assessment
- [ ] Check CFTC positioning data (or equivalent local data for EM). Rapid buildup = warning
- [ ] Monitor cross-market correlations: when unrelated carry trades (e.g., FX carry, rates carry) start correlating, global flows are chasing carry everywhere
- [ ] Test for **asymmetric market response**: does favorable news fail to move in your direction? If yes, too many longs; no marginal buyer on good news, rush for exits on bad news
- [ ] Assess: how long has the low-vol carry environment persisted? Longer = more crowded

### Step 4: Carry-Efficient Alternatives
- [ ] If your directional view carries negative, scan for correlated curve/butterfly/cross-market trades with less carry drag
- [ ] Regress potential alternatives against your target to find beta
- [ ] Compare carry per unit of directional risk across alternatives
- [ ] Example: bearish 2Y (steep negative carry) → try weighted 2s/5s flattener (60% of the risk, less carry cost)

---

## Checklist 2: Relative Value Trade Construction

Use for butterflies, curve RV, bond-level RV, or any mean-reversion trade.

### Step 1: Identify the Dislocation
- [ ] Start with the simple version of the spread (e.g., 50:50 butterfly)
- [ ] Check if the spread is contaminated by level or curve exposure
- [ ] Ask: is this a white-noise-like series at an extreme, or a trending series? Trending = possible structural change, not RV

### Step 2: Construct Neutral Weights
- [ ] Run multiple regression: regress belly yield against wings (or target against correlated instruments)
- [ ] Extract level-neutral and curve-neutral betas
- [ ] The weights will NOT be 50:50 — sectors have different volatilities
- [ ] **Convert risk weights (DV01 weights) to notional weights**: Risk weight × target DV01 = required DV01 per leg. Then: notional = required DV01 / (DV01 per $1M of that instrument)
- [ ] **NEVER confuse risk weights with notional weights** — this is the #1 RV trade error

### Step 3: Regime Check (Critical)
- [ ] Is the Fed (or relevant CB) in a stable regime, or transitioning?
- [ ] **Avoid RV trades during regime transitions**: betas shift, "neutral" weights acquire unintended exposure
- [ ] Example: 2s5s10s butterfly betas from 2006 trended for months in fall 2007 as credit crunch changed relative sector vols
- [ ] Set up ongoing monitoring: if regression residuals start trending, relationship may be breaking

### Step 4: Bond-Level RV (Par Curve Analysis)
- [ ] Fit smooth par yield curve through benchmark issues
- [ ] Compute yield residual for each bond: actual yield − model yield
- [ ] Compare each bond's residual to its **OWN history**, not just to zero
- [ ] Hot runs (on-the-run) systematically trade rich — if average residual is −6bp and current is −2bp, bond is actually 4bp CHEAP vs. its own average

---

## Checklist 3: Hedging Decision Tree

Use when the user needs to hedge duration or rates exposure.

### Step 1: Should I Hedge?
- [ ] Does the position have risks I don't want exposure to?
- [ ] Is the outright exposure vol >> the resulting basis/spread vol after hedging?
- [ ] Accept: lost gain on the hedge leg is expected. The point is lower vol and higher Sharpe

### Step 2: Instrument Selection

| Criterion | Swaps | Treasuries | Treasury Futures | ED Futures |
|-----------|-------|------------|------------------|------------|
| Tracking error in stress | **Better** (widen in stress = helps) | **Worse** (rally in flight-to-quality = double loss) | Moderate (CTD switch risk) | Short end only |
| Flexibility | Any maturity | Benchmark points only | 2Y/5Y/10Y/Long | ≤3Y practical |
| Balance sheet | No up-front notional | Requires repo/funding | Exchange-traded | Exchange-traded |
| Counterparty risk | Bank exposure | None | Clearinghouse | Clearinghouse |

- [ ] **Default to swaps for core hedges** — they underperform in stress, which is what you want
- [ ] Treasuries for tactical overlay only, or when swap spread RV favors it
- [ ] Check BNOC: futures cheap (high BNOC) = poor hedge; futures rich (low BNOC) = good hedge

### Step 3: Calculate Hedge Ratio
- [ ] **DV01-match**: position DV01 / hedge instrument DV01 per $1M = hedge notional
- [ ] Apply **yield beta** adjustment: hedge notional × yield beta (from regression of asset yield changes on hedge yield changes)
- [ ] Monitor yield beta stability — if it breaks down, the hedge instrument is unsuitable in current conditions
- [ ] **Never use notional or market value to calculate derivative hedge ratios** — derivatives are leveraged

### Step 4: Maturity Matching
- [ ] Match hedge maturity to asset maturity as closely as possible
- [ ] If deviating for carry savings, quantify tracking error increase vs. carry benefit
- [ ] For MBS/convexity products: dynamic hedging required — monitor duration changes and rebalance

---

## Checklist 4: Rates View Formation Hierarchy

Use to structure any rates directional view, from macro call to entry point.

### Decades (Background Context — Not Directly Tradeable)
- [ ] Potential growth rate (technology, demographics, productivity)
- [ ] Structural deficit trajectory (aging populations, social programs)
- [ ] Leverage cycle position (rising smoothly, or near discontinuity?)

### Years (Medium-Term Positioning)
- [ ] What Fed/CB regime? Easing → front-end steepens | Tightening → front-end flattens | On-hold → carry/RV dominate
- [ ] Total duration supply/demand: **all** fixed income sectors, not just Treasuries/government bonds
- [ ] Demand source analysis: who is buying and why? (foreign CBs, central bank QE, banks, pension funds, mutual funds, households)
- [ ] Economic cycle position: recession increases supply but also increases demand (flight to quality, weak loan growth)

### Months (Tactical Positioning)
- [ ] Fed/CB regime transition signals — these are the most volatile periods
- [ ] Supply calendar: auction concentration in one sector cheapens it vs. neighbors
- [ ] MBS/mortgage hedging direction: rising rates → extension → pay swaps (rates higher); falling rates → contraction → receive swaps (rates lower)
- [ ] Corporate issuance hedging: heavy issuance → temporary narrowing of swap spreads

### Weeks/Days (Entry/Exit Timing)
- [ ] Economic data calendar: NFP, ISM, CPI/PCE, housing, retail sales
- [ ] FOMC/CB meeting dates: 10Y daily vol = 12bp on FOMC vs 7.4bp normally
- [ ] Flight-to-quality risk: front end receives greatest flows; curve steepens initially
- [ ] Auction cycle: sector facing auction cheapens vs. neighbors (tradeable via butterfly)
- [ ] Seasonality: April tends to see yield increases; Aug/Sep yield decreases. Use only to bolster existing views or time entry

---

## Checklist 5: Swap Spread Analysis

Use when analyzing or trading swap spreads in DM or EM IRS markets.

### Step 1: Map Current Drivers

| Driver | Direction on Spreads | Check Current Status |
|--------|---------------------|---------------------|
| Bank credit stress | Wider (front end) | [ ] Current LIBOR/OIS or equivalent spread? |
| Flight to quality | Wider (front end) | [ ] Risk sentiment? Recent Treasury rally? |
| Treasury/government bond supply | Narrower (5-10Y) | [ ] Recent issuance concentration? Deficit trajectory? |
| Pension demand for long-end | Narrower (30Y) | [ ] Current pension funding status? Regulation changes? |
| Mortgage hedging flows | Wider (5-10Y) in rising rate environment | [ ] MBA Refi Index? Extension or contraction phase? |
| Corporate issuance hedging | Narrower (temporary) | [ ] Seasonal issuance calendar? Heavy week? |
| Exotics hedging | Variable (long end) | [ ] Current structured product popularity? |

### Step 2: Assess Directionality
- [ ] Average directionality: ~7bp spread widening per 100bp yield increase
- [ ] Current regime: is mortgage hedging, flight-to-quality, supply, or recovery the dominant driver?
- [ ] **Warning**: directionality relationship flips between regimes (2005-06 vs 2009)
- [ ] Can hedge directionality by weighting swap/Treasury legs unequally

### Step 3: Spread Curve (Sector Isolation)
- [ ] If trading one spread vs. another (e.g., 2Y spread vs. 10Y spread): DV01-match ALL four legs
- [ ] This hedges out both broad rate moves AND broad spread moves
- [ ] Isolates sector-specific factor (bank credit stress → 2Y; mortgage hedging → 5-10Y; supply → long end)

---

## Checklist 6: Conditional Trade Setup

Use when the user wants to express a curve or spread view only in a specific yield scenario.

### Pre-Conditions
- [ ] Do you have a joint view on (a) direction AND (b) curve/spread behavior in that direction?
- [ ] Is the conditional structure at or better than forwards? If worse → the outright trade is almost always better
- [ ] Is the view horizon < 3 months? Conditional trades should use short expiries (curve/spread directionality is unstable)

### Conditional Curve Trade Construction
- [ ] **Both legs same option type** (both payers for rising rate conditional; both receivers for falling)
- [ ] Buy option on the leg you expect to underperform (e.g., buy payer on 10Y for conditional steepener in selloff)
- [ ] Sell option on the other leg (e.g., sell payer on 2Y)
- [ ] If rates go the wrong way → both expire worthless → no exposure
- [ ] DV01-match notionals so exercise produces a DV01-neutral curve trade
- [ ] Check premium neutrality: if net premium payout → "worse than forwards" → reconsider

### Conditional Spread Trade Construction
- [ ] **Mixed instruments**: swaption on one leg, Treasury/bond option on the other
- [ ] For spread widener in rising rates: buy payer swaption + sell Treasury/bond put (duration-matched)
- [ ] For spread narrower in falling rates: buy receiver swaption + sell Treasury/bond call
- [ ] Match swap to futures contract: forward swap starts on last delivery date, matures on CTD maturity
- [ ] Convert futures option OTM distance to yield terms (divide by duration), set swaption strike same distance OTM
- [ ] DV01-match using option-adjusted or empirical DV01 for futures leg

### Three Setup Rules (All Conditional Trades)
1. **Expiry < 3 months** — directionality relationships are too unstable for longer expiries
2. **DV01-neutral notionals** — at exercise, enter a properly hedged spread/curve trade
3. **Premium neutral preferred** — if you're paying net premium, you're entering at worse-than-forwards. Only proceed if the conditional protection is worth it

---

## Checklist 7: Basis Trade Assessment

Use when evaluating Treasury futures basis trades (long basis = buy cash, sell futures; short basis = sell cash, buy futures).

### Step 1: Identify CTD and Net Basis
- [ ] Which bond is CTD? (highest implied repo rate OR lowest BNOC)
- [ ] What is the BNOC? This is the market's price for the delivery option
- [ ] Compare BNOC to your own delivery option valuation (model or historical)
- [ ] CTD net basis profile: low-duration CTD ≈ call on yields; mid ≈ straddle; high-duration ≈ put on yields

### Step 2: Risk Assessment
- [ ] **Balance sheet**: basis trades collect small ticks, require large positions. Can you maintain position through stress?
- [ ] **Repo**: have you termed out your repo? Rolling overnight is dangerous — repo rates can collapse hundreds of bps during flight-to-quality
- [ ] **Historical context**: selling the basis is historically profitable, but BNOC reached 20+ ticks in 2008 (vs. normal 5). Are you prepared for tail events?
- [ ] **30Y exception**: can go negative (pension fund demand for synthetic duration via futures)

### Step 3: Roll Timing
- [ ] Check CFTC positioning: large commercial longs → calendar spread narrows → longs roll early, shorts roll late
- [ ] Five drivers of calendar spread: yield levels, **financing rates** (most important in volatile times), **positioning** (most important when Fed on hold), CTD curve, relative value
- [ ] Your roll decision depends on your view of the calendar spread direction

---

## Checklist 8: Rate Volatility Trading Framework

Use when trading implied vs realized vol, or when assessing option structures for rates.

### Step 1: Vol Regime Assessment
- [ ] What is the Fed/CB regime? On-hold → vol compresses. Transition → vol spikes
- [ ] Curve shape: steep → higher vol; flat → lower vol; sharply inverted → volatile again
- [ ] Liquidity conditions: abundant → low vol; withdrawal → vol spikes
- [ ] Key P&L formula: net P&L from gamma + theta ∝ (realized vol − implied vol)

### Step 2: Structural Supply/Demand
- [ ] **Long vol demand**: GSE mortgage portfolios (intermediate swaptions), mortgage servicers (short-dated options on 5-10Y)
- [ ] **Short vol supply**: callable debt issuance (agencies sell swaptions), exotics desks (range accruals → sell caps)
- [ ] Which side currently dominates in the sector you're trading?

### Step 3: Strategy Selection
- [ ] **Expiry switch** (same underlying, different expiry): vega-neutral trades implied vol spread; gamma-neutral trades realized vol spread
- [ ] **Tail switch** (same expiry, different underlying): vega-neutral ≈ gamma-neutral (same expiry)
- [ ] **Critical**: for expiry switches, vega-neutral and gamma-neutral produce VERY different risk profiles because short-dated options have more gamma per vega

### Step 4: Three Warnings
1. **Gap risk**: illiquid markets cause P&L to diverge from textbook gamma/theta. Especially dangerous for short vol
2. **Skew**: as underlying moves, implied vol changes — introduces vega P&L into "delta-hedged" positions
3. **Path dependency**: same realized vol can produce different P&L depending on when and where moves occur relative to strike

---

## Cross-Reference: When to Use Each Checklist

| Situation | Primary Checklist | Also Consult |
|-----------|-------------------|-------------|
| Evaluating a carry trade | 1 (Carry) | 4 (View Hierarchy) for context |
| Setting up a butterfly or RV trade | 2 (RV Construction) | 1 (Carry) for carry-to-risk |
| Deciding how to hedge | 3 (Hedging) | 5 (Swap Spreads) for swap vs Treasury decision |
| Forming a macro rates view | 4 (View Hierarchy) | 5 (Swap Spreads) if trading swaps |
| Analyzing swap spreads | 5 (Swap Spreads) | 4 (View Hierarchy) for directional context |
| Expressing conditional view | 6 (Conditional) | 5 (Swap Spreads) for spread conditionals |
| Evaluating basis trade | 7 (Basis) | 1 (Carry) for carry component |
| Trading vol or structuring options | 8 (Vol Trading) | James checklists for FX vol |
| EM rates with DM overlay | 4 (View Hierarchy) | Willer Checklist 2 for EM-specific cycle |
