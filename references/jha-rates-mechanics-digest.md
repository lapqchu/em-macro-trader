# Siddhartha Jha — Interest Rate Markets: A Practical Approach to Fixed Income (Wiley, 2011)
# Structured Digest for em-macro-trader Skill

---

## Metadata

- **Author**: Siddhartha Jha (rates strategist/trader)
- **Publisher**: Wiley (2011)
- **Scope**: Comprehensive practitioner guide to US interest rate markets — bonds, futures, swaps, options, repo, carry/RV trades, hedging, swap spreads, basis trading, conditional trades
- **Why it matters for this skill**: Provides the mechanical/plumbing layer underneath the tactical (Willer), strategic (Booth), and options (James) layers. The user trades EM rates and FX, but 65% of EM returns are driven by DM factors (Willer). Understanding US rates mechanics — curve construction, supply/demand, MBS convexity flows, swap spreads, Fed transmission — is essential for interpreting the global regime that dominates EM P&L. Also enables DM positions and cross-market RV.

---

## Core Thesis

Interest rate markets are driven by the interaction of supply and demand for credit, with the Fed controlling the short end and expectations/flows shaping the long end. Profitable trading requires decomposing every position into its component risks (direction, carry, roll, vol, correlation, liquidity), understanding who else is positioned and why, and structuring trades as specifically as possible to isolate the risk you want. Simple frameworks applied with discipline beat complex models that obscure assumptions.

---

## Layer 1: Bond Mathematics and Conventions

### DV01 — The Core Risk Metric

Think in DV01, never in notional. DV01 = Modified Duration × Dirty Price / 100 (per $1M notional, in dollars per bp). A $100M 2Y position (DV01 ~$190/bp) has far less risk than $100M in 10Y (DV01 ~$800/bp).

**Price-to-yield conversion shortcut**: Divide a price-based measure by duration to get yield terms. Widely used on trading floors.

### Carry Decomposition

Carry = coupon income − financing cost (repo). Computed in price terms, converted to yield by dividing by duration.

**Carry via forwards**: Carry = Forward yield − Spot yield. This is algebraically equivalent to the coupon-minus-financing method.

**Locking in carry**: Use term repo (vs. overnight) to fix the financing leg. With both coupon (fixed by the bond) and financing (fixed by term repo) known, carry is locked.

**Key insight**: Earning full carry requires that the forward yield converges to the current spot yield (curve doesn't move). Forwards are poor predictors, which is why carry tends to be earned — but volatile markets can overwhelm carry.

### Rolldown / Slide

Rolldown = P&L from a bond aging along an unchanged yield curve. Unlike carry, rolldown CANNOT be locked in — it depends on the curve not moving.

**Carry + Rolldown combined** = 3M-forward rate at aged maturity − spot rate at aged maturity. The current yield cancels out.

**Market convention trap**: Participants often say "carry" when they mean carry + rolldown. Always clarify.

### Convexity

Positive convexity = gains > losses for equal yield moves. Longer maturity, lower coupon = more convexity. Convexity is more valuable in volatile markets.

**Negative convexity** (MBS, callables): Gains are capped because the embedded call becomes more valuable as rates fall. Duration extends in selloffs and shortens in rallies — exactly the wrong way.

### Forward Rates

Forward rate = breakeven rate that makes two lending strategies equivalent. Use ZERO-coupon rates, not par rates.

**Quick approximation**: F_{1,2} = [(T1+T2)×R2 − T1×R1] / T2

---

## Layer 2: Market Structure and Instruments

### Federal Reserve Transmission

Fed controls overnight rate → affects financing/repo rate for longer-term assets → expectations of future financing rates shape the entire curve.

**2Y rate** ≈ market expectation of Fed activity over next 2 years. **10Y rate** embeds longer-horizon growth/inflation expectations. Link weakens with maturity.

**Three Fed regimes** (easing, on-hold, tightening) produce distinct curve dynamics:
- **Easing**: Front-end steepens sharply, back-end follows with lag
- **Tightening**: Front-end flattens, long end doesn't rise as fast (hikes cut growth expectations)
- **On-hold**: Carry and RV trades dominate; front-end compresses as investors reach for yield

### Treasury Market

Auction process (Dutch auction, single-price allocation), on-the-run vs off-the-run dynamics, constant maturity Treasury rates. When-issued trading for price discovery.

**Maturity allocation of issuance**: Crises spike bill issuance (short-term, easy to digest). Over time, Treasury extends average maturity back to 6-7Y to avoid rollover risk. Concentration of issuance in one sector cheapens it vs. neighbors.

### MBS and Convexity Hedging — The Flow Monster

Mortgage portfolios have negative convexity from the prepayment option. Hedgers must dynamically rebalance:
- Rates fall → MBS duration shortens → sell duration (sell Treasuries, pay fixed in swaps)
- Rates rise → MBS duration extends → buy duration (buy Treasuries, receive fixed)

This creates a **positive feedback loop** that amplifies rate moves. The aggregate MBS universe is large enough to move the entire Treasury/swap market.

**Mortgage servicing assets (IOs)** have negative duration AND negative convexity — their hedging flows add to the same feedback dynamic.

### Interest Rate Swaps

Swap rate = weighted average of forward LIBOR rates. Fixed leg ≈ bond; floating leg resets to par on each coupon date.

**Swap duration** = Fixed leg duration − 0.25 (for quarterly float). DV01 at inception = duration × 100.

**Swaps vs Treasuries for hedging**: Swaps tend to underperform in stress (bank credit widens spreads), which is exactly what you want in a hedge. **Treasuries fail as hedges in flight-to-quality** because they rally while the asset falls — you lose on both legs (2008 muni example).

### Interest Rate Futures

**Eurodollar futures**: $25/bp, cash-settled against 3M LIBOR. Convexity bias makes ED rate > FRA rate, growing with maturity.

**Treasury futures**: Physically settled, CTD mechanism. CTD = highest implied repo rate = lowest BNOC. Gross basis = carry + delivery option value. Futures display negative convexity (track lowest-price bond in basket).

**Fed funds futures**: Monthly, settled on average daily effective fed funds rate. Extract rate hike/cut probabilities: P(25bp cut) = (Target − FF rate) / 0.25. Adjust for day-weighting when multiple meetings fall in one month.

---

## Layer 3: Drivers of Interest Rates

### Long-Term: Supply/Demand Framework

**Demand side**: Inflation expectations are the dominant risk for holders. The potential growth rate is the long-term anchor. The leverage cycle creates discontinuities (Greece: years of rising debt with declining rates, then sudden reversal).

**Supply side**: Total duration supply (not just Treasury supply) is what matters — issuance volume × average duration across all fixed income sectors. The 2009 lesson: Treasury yields stayed low despite record issuance because net supply in other sectors (ABS, agencies) was falling.

### Demand Sources — Who Buys and Why

| Buyer | Share of Treasuries | Primary Driver | Trading Implication |
|-------|-------------------|----------------|---------------------|
| Foreign CBs | ~50% | Trade surplus recycling, FX reserve management | Monitor Fed custody data; fear of "dumping" overstated |
| Federal Reserve | Variable (QE-dependent) | Monetary policy, portfolio balance channel | QE announcements immediately lower rates across curve |
| Mutual funds | ~9% | Benchmarking, flight-to-quality, curve steepness | Most volatile at margin; watch around heavy auction schedules |
| Banks | Variable | Loan demand inverse (weak economy → buy Treasuries), regulatory requirements | Post-crisis structural shift toward Treasuries; watch loan growth |
| Pension funds | Structural long-end bid | Asset-liability matching, 20-30Y demand | Compresses long-end yields structurally |
| Households | ~10% | Savings rate, risk aversion | Surge during equity declines; sticky once allocated |

### Short-Term Drivers (Days to Weeks)

1. **Economic data**: Employment (NFP), manufacturing (ISM), inflation (CPI/PCE), housing, consumption
2. **Fed events**: FOMC volatility (10Y daily SD: 12bp on FOMC vs 7.4bp normally)
3. **Flight to quality**: Front end receives greatest flows; curve steepens initially
4. **Auction cycle**: Sector facing auction cheapens vs. neighbors (tradeable via butterfly)
5. **Mortgage hedging flows**: Pro-cyclical positive feedback; can dominate for months
6. **Exotics hedging**: Affects long-end spreads; varies with structured product popularity
7. **Seasonality**: April tends to see yield increases; Aug/Sep yield decreases. Use only to bolster existing views or time entry.

---

## Layer 4: Trade Construction

### Carry Trades

**Evaluation metric**: Carry-to-risk ratio = annualized carry / annualized vol of yield changes.

**Hedged carry trades** (curve trades, butterflies) often have lower absolute carry but higher carry-to-risk — they are more efficient.

**Four decision rules for carry trade risk management**:
1. Calculate carry-to-vol using STRESS-period volatility, not recent calm
2. Track CFTC positioning — rapid buildup = warning
3. Monitor cross-market correlations — when unrelated carry trades correlate, flows are global
4. Watch for asymmetric market response — favorable news fails to move in your direction = crowded

### Relative Value Trades

**2s/5s/10s butterfly construction**: Regress 5Y yield against 2Y and 10Y to find level-neutral and curve-neutral weights. Convert risk weights (DV01) to notional weights. Trade the residual for mean reversion.

**Critical pitfall**: Beta instability during regime transitions. If the Fed shifts from on-hold to easing, regression betas shift and "neutral" weights acquire unintended exposures.

**Par curve analysis**: Fit smooth fair-value curve, compute yield residuals per bond. Compare each bond's residual to its OWN history, not just to zero (hot runs trade systematically rich).

### Carry-Efficient Directional Trades

When your view carries negative, scan for correlated trades with less carry drag. Example: bearish 2Y (steep negative carry) → try a weighted 2s/5s flattener (similar directional exposure, less carry cost per unit of risk).

### Conditional Trades

Use options to express curve or spread views only in specific yield scenarios. If yields go the wrong way, options expire worthless — no exposure.

**Construction**: Buy payer swaption on one leg, sell payer swaption on other leg. If rates fall, both expire worthless. If rates rise, exercised into DV01-neutral curve trade.

**Three setup rules**: (1) Expiry < 3 months, (2) DV01-neutral notionals, (3) Premium neutral preferred. If worse-than-forwards, do the outright instead.

---

## Layer 5: Swap Spreads

### What Drives Swap Spreads

| Driver | Wider/Narrower | Maturity Affected |
|--------|---------------|-------------------|
| Bank credit stress | Wider | Front end (2Y) |
| Flight to quality | Wider | Front end |
| Budget deficit / Treasury supply | Narrower | 5-10Y |
| Pension demand for long-end | Narrower | 30Y |
| Mortgage hedging (rising rates) | Wider | 5-10Y |
| Corporate issuance hedging | Narrower (temporary) | Broad |

**Directionality**: Swap spreads widen ~7bp per 100bp yield increase on average (mortgage hedging). But relationship flips in crisis/recovery regimes.

**30Y spreads went negative in 2008** — driven by pension fund receiving, not credit commentary.

### Spread Curve Trades

Four legs: trade one spread vs. another to isolate sector-specific factors. DV01-match all legs. Useful for auction-driven dislocations, mortgage hedging concentration in specific sectors.

---

## Layer 6: Interest Rate Options and Volatility

### Rate Option Conventions

Normal (Bachelier) model preferred for rates (bp/year). Black (lognormal) model for price-based options (Treasury futures, Eurodollars). Conversion: normal vol = lognormal vol × forward rate.

### Key Products

**Swaptions**: Right to enter swap at expiry. Single-look. Receiver = benefits from lower rates. Payer = benefits from higher rates. Notation: 1Y×2Y = 1-year expiry, 2-year swap tail.

**Caps/Floors**: Chain of caplets on LIBOR. Multilook. Notation: 1×3 cap = starts in 1 year, caps for 2 years.

**Treasury futures options**: Exchange-traded. Only front contract liquid.

### Implied vs Realized Vol

Net P&L from gamma + theta ∝ (realized vol − implied vol). Implied vol = breakeven movement level. Long option profits if realized > implied. Short option profits if realized < implied.

### Three Critical Warnings

1. **Gap risk**: Illiquid markets cause P&L to diverge from textbook gamma/theta formulas
2. **Skew**: As underlying moves, implied vol changes — introduces vega P&L into "delta-hedged" positions
3. **Path dependency**: Same realized vol produces different P&L depending on when moves occur relative to strike

### Structural Supply/Demand for Rate Vol

**Long vol demand**: GSE mortgage portfolios (buy intermediate swaptions), mortgage servicers (buy short-dated options on 5-10Y)
**Short vol supply**: Callable debt issuance (agencies sell swaptions), exotics desks (range accruals → sell caps)

### Vol Trading Strategies

**Expiry switches** (same underlying, different expiry) and **tail switches** (same expiry, different underlying).

Weighting: vega-neutral trades implied vol spread; gamma-neutral trades realized vol spread. For expiry switches, these produce very different risk profiles because short-dated options have more gamma per vega.

---

## Layer 7: Treasury Futures Basis and Rolls

### Basis

BNOC = Gross basis − Carry = Delivery option value. CTD net basis profile resembles calls (low-duration CTD), straddles (mid), or puts (high-duration CTD) on yields.

**Selling the basis is historically profitable** (market overvalues delivery option) but can produce catastrophic losses in stress (BNOC reached 20+ ticks in 2008 vs normal 5).

### Rolls

Five drivers: yield levels, financing rates (MOST IMPORTANT in volatile times), positioning (MOST IMPORTANT when Fed on hold), CTD curve, relative value.

**Decision**: Large commercial longs → calendar spread narrows → longs roll early, shorts roll late. Reverse for commercial shorts.

---

## Cross-Reference with Existing Skill Sources

### Where Jha Agrees with Willer
- Carry is the gravitational pull on positions — both emphasize carry decomposition as the first analytical step
- Global regime (DXY, US rates, US HY) drives 65% of EM returns — Jha provides the machinery behind the US rates component
- Positioning data is a lagging but important crowding signal (Willer: breadth/momentum; Jha: CFTC COT)
- Event calendars (CB meetings, data releases, auctions) create tradeable short-term patterns

### Where Jha Extends Willer
- **Curve construction mechanics**: Willer says "receive 5Y" or "steepener." Jha explains how to actually build the curve, compute carry + rolldown, set up DV01-neutral structures, and calculate hedge ratios
- **MBS convexity flows**: Willer doesn't cover this. Jha shows how mortgage hedging creates positive feedback loops that amplify rate moves — this affects EM through the US rates channel
- **Supply/demand framework**: Jha maps who buys Treasuries and why — foreign CBs (50%), Fed, banks, pensions, funds. This is the demand side behind the 65% global factor
- **Swap spread dynamics**: Not in Willer. Jha explains what drives swap spreads wider or tighter — directly relevant when the user trades IRS (which are swap-based, not Treasury-based)
- **Conditional trades**: Willer uses options as hedges. Jha shows how to express curve/spread views conditionally using swaption combinations — more targeted risk-taking

### Where Jha Extends Booth
- **Institutional mechanics behind DM demand for "safe" assets**: Booth argues DM sovereign risk is underpriced because of financial repression. Jha shows the specific mechanics — bank regulation forcing Treasury purchases, pension fund ALM demand, Fed balance sheet expansion
- **What "safe" actually costs**: Jha quantifies carry, roll, and opportunity cost of holding Treasuries — useful for Booth's framework comparing EM vs DM risk-adjusted returns

### Where Jha Extends James
- **Rate options vs FX options**: James covers FX option payoff/premium empirics. Jha covers rate option mechanics — swaptions, caps, delta hedging, skew. Combined, the user has both FX and rates option capability
- **Conditional trades**: James doesn't cover this. Jha shows how to use options to express rates views only in specific scenarios — powerful for macro trades where the user has a joint view on level and curve

### Where Jha Differs
- **US-centric**: Jha writes about US Treasuries, LIBOR, Fannie/Freddie. Conventions differ in EM (day counts, fixing mechanisms, NDF dynamics). Apply Jha's frameworks with local convention adjustments
- **Pre-SOFR**: Jha writes during the LIBOR era. The skill should note that SOFR has replaced LIBOR as the dominant reference rate, but the analytical frameworks transfer intact

---

## Method Transfer Notes

### What This Source Teaches About How to Think

1. **Decompose every position**: Direction + carry + roll + vol + correlation + liquidity. Never evaluate a trade on direction alone.
2. **Think in DV01**: The only correct unit for comparing risk across maturities, instruments, and markets.
3. **Carry + rolldown is the breakeven**: This is what the curve can move against you before you lose money. Compute it for every position.
4. **Specificity improves Sharpe**: Each layer of hedging (outright → spread → butterfly → conditional) removes unwanted risk. Absolute return falls but risk-adjusted return rises.
5. **Know your flows**: Mortgage hedging, pension ALM, foreign CB reserves, corporate issuance — these mechanical forces drive short-term rates and can overwhelm fundamental views.
6. **Forwards are poor predictors**: This is the carry trade foundation. It applies in both DM (Jha) and EM (Willer, James).
7. **Swaps are better hedges than Treasuries in stress**: Treasuries rally in flight-to-quality, creating double losses.
8. **Track positioning for crowding**: CFTC data, asymmetric market response, cross-market correlation spikes — all signal crowded trades.
9. **Beta instability kills RV trades**: Regression-based weights only hold in stable regimes. Monitor continuously during Fed transitions.
10. **Balance sheet and liquidity are hidden risks**: Small-tick strategies (basis, RV) require position size → require balance sheet → fail when capacity evaporates.
