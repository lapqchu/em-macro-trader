# Digest: Trading Fixed Income and FX in Emerging Markets

## Metadata
```
Title: Trading Fixed Income and FX in Emerging Markets: A Practitioner's Guide
Author(s): Dirk Willer (Citi), Ram Bala Chandran, Kenneth Lam (Citi)
Publication date: October 2020
ISBN: 978-1-119-59905-0
Scope: EMFX, EM local rates, EM hard currency credit, portfolio construction, event trading
Ingested: 2026-04-16
```

## Table of Contents
1. [Core Thesis](#core-thesis)
2. [Analytical Framework](#analytical-framework)
3. [Key Concepts and Definitions](#key-concepts-and-definitions)
4. [Tradeable Frameworks — EMFX](#tradeable-frameworks--emfx)
5. [Tradeable Frameworks — EM Rates](#tradeable-frameworks--em-rates)
6. [Tradeable Frameworks — EM Credit](#tradeable-frameworks--em-credit)
7. [Event Trading Playbooks](#event-trading-playbooks)
8. [Portfolio Construction](#portfolio-construction)
9. [Quantitative Thresholds and Benchmarks](#quantitative-thresholds-and-benchmarks)
10. [Contrarian and Non-Consensus Views](#contrarian-and-non-consensus-views)
11. [Limitations and Blind Spots](#limitations-and-blind-spots)

---

## Core Thesis

The authors argue that EM is a **top-down, globally-driven asset class** where approximately **65% of returns in FX, credit, and equities are explained by global macro factors** (DXY, US HY spreads, commodity cycles, China stimulus). The critical exception is **EM local rates, where only 36% is global** — rates are dominated by local central bank cycles.

The central operating principle: **trade the cycle, not the structural story**. The era of structural spread compression and structural EM convergence is over. Alpha comes from timing rate cycles, exploiting event-driven dislocations, and disciplined factor-based country selection — not from buying EM and waiting.

The book is organized around three asset classes (FX, rates, credit) with a unified macro overlay, and the analytical method is overwhelmingly **empirical and backtested** rather than theoretical. Every claim is accompanied by information ratios, Sharpe ratios, or return distributions.

---

## Analytical Framework

### The Authors' Decision Hierarchy

**Step 1: What is the global macro regime?**
- DXY direction (dominant driver for EMFX, relevant for credit)
- US HY spreads (most reliable macro leading indicator for EM — better than VIX)
- China stimulus (credit impulse + monetary conditions → commodity prices → EM)
- Fed policy (indirect via DXY and risk appetite, NOT via rate differentials)

**Step 2: Which asset class benefits?**
- Bullish US rates → EM rates outperform EM credit
- Bullish EUR → overweight CEEMEA over Asia
- Bullish commodities → overweight Latam over Asia
- Risk aversion rising → barely hurts EM rates; destroys EMFX and credit

**Step 3: Country selection within asset class**
- FX: volatility-adjusted carry, growth surprises, technicals (momentum, breadth), seasonals
- Rates: central bank cycle position, real rate valuation, term premium, curve shape
- Credit: carry + momentum (vol-adjusted), rating sweet spot (BB, 3-5yr), valuation vs. ratings curve

**Step 4: Trade structure**
- Outright vs. relative value vs. curve vs. options overlay
- Funding currency matters enormously (JPY > EUR > USD for carry)
- Duration bucket matters for credit (front-end leveraged > back-end unleveraged)

### How the Authors Reason

The method is consistently:
1. State a hypothesis (e.g., "carry works")
2. Build a systematic backtest with precise rules
3. Report information ratio, Sharpe, return distribution
4. Show where it breaks (time period decomposition)
5. Propose improvements (volatility adjustment, regime overlay, combination with other factors)
6. State clearly when something doesn't work

They treat every "obvious" market belief as testable and frequently find conventional wisdom is wrong. Their standard of evidence is quantitative: if the IR is negative or unstable, the strategy doesn't work regardless of how intuitive it sounds.

---

## Key Concepts and Definitions

### The 65/35 Split
- 65% of EMFX, EM credit, and EM equity returns explained by global macro
- 36% of EM rates explained by global macro (64% local)
- This is the foundational allocation of analytical effort

### "True EM" vs. G10-Like EM
- Defined by behavior, not GDP: **if a currency's rates differential strategy has negative IR, it is "true EM"**
- True EM: BRL, MXN, COP, PEN, TRY, RUB, ZAR, HUF, TWD
- G10-like EM (positive rate differential IR): KRW, INR, THB, MYR, SGD, PHP
- The litmus test: "The behaviour of rates during risk aversion is the litmus test for whether a country is a developed market"

### Information Ratio as Core Metric
- Average return / standard deviation (pre-funding cost)
- Used throughout to normalize across strategies with different leverage
- Authors emphasize IR over raw returns because leverage is adjustable; risk-adjusted alpha is not

### Carry (Precise Definition)
- FX: forward points (spot-forward differential), NOT interest rate differential
- Bonds: yield minus funding cost (repo or Libor)
- Breakevens: nominal yield minus real yield
- The distinction matters because cross-currency basis makes these diverge
- Simple carry on USD funding has been MONEY-LOSING since 2011 (despite higher nominal yields); JPY-funded carry outperforms by 200-400% over a full cycle; EUR-funded sits in between
- Carry levels need to return to ~5-6% (2004-era levels) for the simple strategy to work again on USD funding

### Roll-Down
- The book treats roll-down as an implicit component of rates P&L but does not develop a standalone roll-down framework
- For IRS: roll-down benefit depends on curve steepness — a steep curve gives positive roll-down for receivers
- The "sliding down the slope" chapter (6.21) addresses curve slope valuation: regress 2s/5s on 2s; rank residuals across countries; long steepest 5 / short flattest 5; volatility-adjust — shows value but Sharpe insufficient for standalone
- Roll-down is most relevant for linker investors where long duration (avg 14Y in Brazil vs. 4.8Y nominals) means meaningful roll if curve is stable

### Volatility-Adjustment
- Position sizing by inverse prior-year realized volatility
- Applied to: carry baskets, momentum signals, credit country weights
- Consistently improves IR by 30-50% across strategies
- Two levels in credit: (1) volatility-adjust the momentum calculation itself, (2) volatility-adjust the position weight — both help

### Risk Overlay for Carry
- Construct max z-score (2yr lookback) across 5 vol surfaces: EMFX IV, G10 FX IV, US rates IV, S&P 500 IV, oil IV
- When max z-score >2 std dev: cut EMFX carry exposure entirely
- When <2 std dev: re-enter
- This overlay significantly improves returns on the volatility-ranked carry basket

### ML/Systematic Strategy Findings
- Random Forest: IR 1.24 for EMFX signals (vs. mean traditional signal IR 1.04)
- Gradient Boosting: IR 1.20
- Voting Classifier (RF, LR, SVM, GB, KNN): IR 1.26
- Test case: predict weekly BRL returns using economic surprise indices + technicals via classifiers
- Best practical use: fundamental researchers use ML to identify features, validate against logic, add to existing models (human + machine beats pure machine)
- Core problem: limited time-series data for financial instruments; high overfitting risk; cross-sectional better suited than time-series for ML (only ~100 investable countries)
- CPI nowcasting identified as highest ROI big data application for EM rates (local rates 64% driven by local factors; web scraping retail prices improving with e-commerce growth)
- Chinese activity data (cargo tracking, satellite, shipping containers) identified as second-highest ROI for spillover effects on EMFX/credit

---

## Tradeable Frameworks — EMFX

### Factor Hierarchy (by Efficacy)

| Factor | IR (Long-Only, Vol-Adj) | Notes |
|--------|------------------------|-------|
| Growth surprises | ~0.86+ | Best standalone signal; Citi surprise index crossing zero from below |
| Seasonals (10yr lookback, >1% threshold) | ~1.0 aggregate | Weekly rebalance; ZAR, ILS, CLP, SGD, KRW, THB top performers |
| Breadth | ~1.0 | Count of up vs. down days; trend confirmation, not early signal |
| Vol-adjusted carry (JPY-funded) | 1.16 | Long top 4 by carry/vol; broken on USD funding since 2011 |
| Momentum (1-month) | 0.86 (vol-adj) | Degraded vs. pre-2008 but still tradable |
| PPP valuation (10yr lookback) | 0.35 | REER is worse (negative IR); ToT-adjusted REER improves to 0.4 |
| Current account | Negative | Money-losing as standalone; only useful as complement to carry |
| Interest rate differentials | Negative | **Does not work for EM** — inverse of G10; most dangerous mistake |

### Risk Overlay
- Max z-score (2yr lookback) across: EMFX IV, G10 FX IV, US rates IV, S&P IV, oil IV
- Cut exposure when >2 std dev; re-enter when <2 std dev
- Significantly improves carry strategy returns

### Low-Cost Hedge Basket
- Identify currencies with beta >1 to EMFX index + negative or low carry
- As of 2018: HUF, SEK best; add EUR, CZK for diversification

### Positioning as Momentum (Not Contrarian)
- "Consensus usually works" — 7 of 10 positioning percentiles show positive forward returns
- Very long MXN when positioned long → positive returns (2.4-4.1% over 3 months)
- Flows are **lagging**, not leading — Asia FX leads equity flows, not vice versa

### China as Leading Indicator
- 200-day MA z-scores of Chinese monetary conditions + credit impulse vs. commodity EMFX basket — extended deviations signal mean reversion (e.g., 2017 fading stimulus took months for FX to catch down)
- 12-month CNH forward >5% weaker than spot = extended short positioning (inflection signal)
- PBOC fix: 10bp persistent forecast error on 5-day MA signals policy intent; markets typically obey without fighting large FX reserves and capital controls
- CGBs lead UST at cycle troughs, lag at peaks: bottom in Chinese rates = bullish signal for risk assets. Specific historical leads: 2009 China bottomed before UST; 2016 China bottom preceded US by 6 months; March 2018 Chinese rally signaled US rate sell-off was mature
- Chinese rates residual threshold: regress 52-week rolling Chinese rates on US rates; residuals above +50bp signal Chinese rate peak; below -50bp signal Chinese rate trough
- China export dependency by country GDP: Vietnam 22.9%, Malaysia 17.4%, Korea 11.5%, Singapore 10.6%, Thailand 9.1% — these countries have structural leverage to Chinese growth
- MXN has near-zero beta to CNH — safest EM from China shocks; commodity currencies (ZAR, CLP, COP) show betas 0.5-0.9
- China's August 2015 1.9% devaluation: S&P fell 10% in 4 days, US 2Y rates fell 19bp, directly altered Fed policy (no September 2015 hike despite plans)

---

## Tradeable Frameworks — EM Rates

### The Core Rate Cycle Rules

**Easing Cycle ("Receive Around the Last Hike Until the Last Cut is Close")**
- Enter: When 1yr swap crosses below policy rate from above (turn signal)
- Confirm: Last hike + inflation showing directional change downward
- Hold: Through easing cycle until ~1 cut remaining
- P&L: Strongly positive; carries well as curve normalizes

**Hiking Cycle ("Pay Into the First Hike Until the Last Hike is Close")**
- Enter: ~20 trading days BEFORE first hike (not after)
- Hold: Until last hike has occurred
- Payers less profitable than receivers (risk premium works against you)

**Critical Empirical Finding**: EM central banks stop hiking in the **same month** inflation peaks (median). At first cut, inflation is still ~130bp above upper target band — direction matters more than level.

### Curve Trades

**Steepeners (Receivers for Chickens)**
- 2s/10s steepeners start working several months BEFORE first cut
- Better Sharpe than outright receivers; lower carry drag
- EM advantage: risk aversion steepens curves → natural hedge
- Cash-constrained investors: position in the long end during bull steepening (more duration) despite curve steepening bias
- 1s/2s special behavior: FLATTEN after last hike (front end has no DV01 left, ~10-month average gap between last hike and first cut); STEEPEN after last cut (steepeners work in "boring" periods)
- 1s/2s requires constant DV01 reweighting due to fast roll-down of 1Y maturity

**Flatteners (Payers for Chickens)**
- 2s/10s flatteners work going INTO first hike
- Less reliable than steepeners; worse performance
- 1s/2s: reverse of easing — steepen after last cut, before first hike

### Central Bank Constraints (Why EM Rates Are Different from DM)

**FX Pass-Through (Most Critical)**
- EM pass-through 2-3x higher than DM
- Cannot be bullish EM rates and bearish EMFX simultaneously in credit-sensitive countries
- Higher food/energy CPI weights (~30% Peru vs. <10% US) amplify commodity shocks

**Commodity Constraint**
- Global commodity prices dominate EM inflation variance: Asia 83%, CEEMEA 61%, Latam 55%
- **Exception for commodity exporters**: Higher commodities → stronger currency → lower tradables inflation
- Receivers work during commodity rallies in commodity exporters (counterintuitive)

**Fed Constraint**
- Fed hikes → stronger USD → weaker EMFX → higher inflation → EM forced to hike despite domestic weakness
- Exceptions exist: EM can cut during benign Fed hiking cycles (slow hikes, strong global growth)

### Valuation and Risk Premia

**Term Premium**: When >1 std dev elevated (3-month rolling) → receive 5Y; Sharpe improves from 0.88 (buy & hold) to 1.18

**Real Rate Valuation**: Rank countries by real yields; long top 3 / short bottom 3; best metric is inflation target midpoint as deflator

### Real Rates (Linkers)

**Core Findings**:
- Duration-adjusted, linkers have lower vol than nominals
- IR: linkers 1.62 vs. nominals 1.47 (2009-2018) — leverage linkers rather than hold nominals
- **Own nominals** during easing cycles and UST rallies
- **Own linkers** during hiking cycles, commodity rallies, and EMFX sell-offs

**Breakeven Entry/Exit Thresholds**:
- Buy when 5Y breakevens < inflation target midpoint (rare: 5-8% of time)
- Sell when 5Y breakevens > current inflation by 1.5-2.5%
- Brazil: buy below 4.5%; Mexico: buy below 3.0%; Chile: buy below 3.0%

---

## Tradeable Frameworks — EM Credit

### Factor Hierarchy

| Factor | IR | Notes |
|--------|-----|-------|
| Vol-adjusted carry (long HY / short IG) | Positive | Still works (unlike EMFX carry post-2013) |
| 12-month vol-adjusted momentum | 0.7 | Monthly rebalance; avoids 2008 drawdown |
| Ratings valuation (vs. exponential curve) | Sharpe 0.9 (L/S) | Long 5 cheapest vs. 5 most expensive by rating residual |
| Long-only EMBI | 0.38-0.40 | Benchmark |

### The Sweet Spot
- **Rating**: BB is apex (IR 0.89), then A (0.70), B (0.72), BBB worst (0.46)
- **Duration**: 3-5yr (IR 1.32), front-end leveraged outperforms back-end unleveraged
- **Combined**: BB 3-5yr is the structural sweet spot

### Buffett Trade in EM Credit
- Leverage short-duration bonds to match risk of long-end HY
- Front-end substantially outperforms in excess return space
- Improve timing with US manufacturing ISM: when ISM peaks (high 50s) → shift from HY to IG, reduce duration

### Dalio Credit Selection
- **Pegged FX currencies with commodity exposure** = worst credits during commodity downturns
- Best shorts when bearish oil: pegged oil producers

### Defaults
- EM sovereign default probability: 2.5% (1983-2016) vs. US HY 4.2%
- Recovery: 65% sovereigns vs. 37% US HY
- **Post-default 1-year median return: 16% (11% excess over index)**
- Default period shortened to max 2 years post-1998
- Government change in 40%+ of default cases

### Rating Agency Rules
- Downgrades: spreads widen 60 days pre-event; move largely priced by event date
- **1st IG loss**: wait for pullback, then short (92% chance of 2nd downgrade within 6 months)
- **2nd IG loss**: buy 2-3 days post-event (peak negativity, forced selling complete)
- **1st IG upgrade**: go long (strong follow-through)

### US Curve as Credit Timing Signal
- Long EM credit most of the time
- Cut on UST curve **disinversion** if US-centric problem
- Cut earlier on curve **inversion** if EM crisis driving Fed cuts

---

## Event Trading Playbooks

### FX Intervention
- Small country: go with intervention regardless of size
- Large country: require >USD 2.5B/day (Brazil) or rarity (Mexico)
- Brazilian threshold: >1.5% underperformance over 5 days triggers intervention
- Mexican threshold: ~1% over 15 days
- Hold period: ~10 trading days for outperformance vs. EMFX index

### Emergency Rate Hikes
- **Precondition for success**: currency must have experienced >30 daily std dev moves (100-day period) AND REER must be negative (cheap)
- Success rate: 12 of 20 emergency hikes "worked"
- Failure pattern: if currency still expensive (REER positive), sell-off continues post-hike
- For rates: avoid receiving day 1; peak sell-off at day 30-50; START receiving around day 50-75
- Full unwind of 200-300bp emergency hike takes ~1 year

### IMF Packages
- FX: weakness continues 5-25 days post-announcement; median turns positive at ~25 days; full stabilization ~3 months
- Credit: spreads widen 130bp average pre-announcement; stabilize 15 days before (rumor leak); post-announcement still widen 50bp before recovery; **150 trading days post = median 100bp+ tightening**
- Rule: wait for first pullback post-IMF announcement before going long

### Elections
- Currency sells off starting 6 months before; accelerates at 3-month mark
- **Trend reverses 2 weeks before election**, followed by strong rally
- Pattern holds even for market-unfriendly winners (Chavez, AMLO)
- Theory: political economy forces market-unfriendly leaders to "boil the frog slowly"
- Trade: fade pessimism ~2 weeks before; long 3 months post

### Data Releases
- **US data hierarchy**: CPI > FOMC > Manufacturing ISM > NFP (NFP is noise for EMFX)
- Follow-through: ~0.7-0.8% EMFX weakness from hawkish surprise over 20 days
- EM inflation data: 1-1.5 additional std dev follow-through over 20-25 days
- CB meeting surprise (2+ std dev move in 2Y on day): dovish → 1.5 std dev follow-through; hawkish → 1.0 std dev
- Chinese data: unreliable; avoid as short-term signal

### Index Inclusion (Rates)
- Bonds: rally 50-100bp post-announcement; 10-50bp additional on actual inclusion
- FX: minimal impact
- Don't take profits until 50%+ of target value actually included

### Domestic Disasters
- 2Y receivers rally 20-50bp over first 5 days (market expects easing concern)
- Peak ~20 days; 80%+ revert over next month
- Only 2 of 7 disasters led to actual CB easing

---

## Portfolio Construction

### Benchmark Critique
- Market-cap weighting rewards faster debt issuance (potentially profligate governments)
- **Equal-weighting outperforms** (IR 0.49 vs. EMBI 0.38)
- **Inverse GDP weighting > cap-weighting** (smaller countries carry risk premium)

### Frontier Markets
- NEXGEM IR 1.42 vs. EMBI 1.38 (slightly higher; mostly B-rated version of EMBI)
- Bull market trade; hedge with liquid EMBI during downturns

### Allocation Methods
- Risk parity (equal-vol weighting): underperforms simple 50-50 GBI-EM/EMBI blend
- Equal-volatility risk parity: IR 1.31 for EMFX (best)
- Hierarchical Risk Parity: IR 1.23 for EMFX (promising for diversification)
- Avoid Black-Litterman (unreliable return forecasts); use covariance-based approaches

### Derivatives as Alpha Source
- Enable curve trades, DV01-neutral strategies
- Swap spreads mean-reverting → diversified alpha
- Tax efficiency (Brazil, Colombia, Indonesia withholding taxes)
- Separate rate and FX bets independently

### ESG
- ESG index performance identical to non-ESG (free lunch, no alpha cost)
- Must control for development stage (GDP/capita) when scoring environmental metrics
- Focus on changes in ESG scores, not levels
- Single-factor ESG funds clearer than aggregated scores

---

## Quantitative Thresholds and Benchmarks

| Metric | Threshold / Value | Signal / Use |
|--------|-------------------|-------------|
| Global macro explanatory power — FX/credit | 65-66% | Top-down required |
| Global macro explanatory power — rates | 36% | Bottom-up can work |
| VIX-EMFX beta warning | Approaches 0 or negative | Defensive positioning |
| UST sell-off threshold | >100bp in 3 months | Reliably EMFX negative |
| Risk overlay cut signal | Max z-score >2 std dev (5 asset IV) | Cut EMFX exposure |
| Brazilian intervention trigger | >1.5% underperformance / 5 days | Expect intervention |
| Emergency hike success condition | >30 daily std dev + REER negative | Hike likely to work |
| Carry strategy vol-adjustment | Inverse prior-year realized vol | Improves IR 30-50% |
| 12-month CNH forward warning | >5% weaker than spot | Extended shorts |
| PBOC fix signal | 10bp persistent forecast error | Policy intent |
| EM CB last hike timing | Same month as inflation peak | Precision for cycle timing |
| Inflation at first cut | ~130bp above upper target band | Direction > level |
| Term premium receiver signal | >1 std dev (3mo rolling) | Receive 5Y |
| Breakeven buy signal | <inflation target midpoint | Rare (5-8%); high conviction |
| IG loss 2nd downgrade probability | 92% within 6 months | Short after 1st IG loss |
| Post-default 1yr return | 16% median (11% excess) | Buy post-restructuring |
| Credit sweet spot | BB, 3-5yr | IR 1.32 |
| Election trend reversal | 2 weeks before election | Fade pessimism |
| IMF credit tightening | 100bp+ over 150 trading days | Patient long |
| EM sovereign default rate | 2.5% (vs. US HY 4.2%) | Structural advantage |
| Recovery rate | 65% (vs. US HY 37%) | Less loss given default |

---

## Country Case Studies (Pattern-Matching Reference)

These are specific historical episodes from the book that illustrate framework application. Useful for analogy when evaluating similar situations.

**Brazil 2011 Easing ("Sugarloaf Mountain")**
- Last hike: July 2011 at 12.25%; 1Y rates were already below CB rate on day of last hike (turn signal confirmed)
- Inflation peak: September 2011 (7.12%); CB cut August 31, 2011 — BEFORE peak inflation
- Back-end sold only 13bp on first cut day before following front end lower
- Result: 12+ months of positive carry receivers; CB credibility intact
- Lesson: when the turn signal fires and CB has credibility, the receiver trade works even if inflation hasn't technically peaked yet

**Brazil 2014-2016 (Dilma / Lava Jato)**
- Despite dramatic local political risk (re-election uncertainty, scandal, impeachment), USD/BRL moved almost identically to the broader EMFX index
- Lesson: local stories have alpha only in relative value terms (e.g., BRL vs. COP at equivalent vol), not in directional FX calls — the 65% global dominance held

**Colombia Oil Shock 2015-2016**
- Oil down 45% → GDP growth from 4.5% trend to 2.0%
- COP depreciated 46% (mid-2014 to early 2016)
- Banrep hiked to 7.75% despite recession-level growth (FX pass-through constraint)
- Lesson: for commodity exporters under FX pressure, the CB is forced to hike even when growth collapses — cannot be bullish rates and bearish FX simultaneously

**India 2013 (Fragile Five Escape)**
- Trade balance inflection (12-month rolling MA trend reversal) was the key signal, not the CA level
- Gold tariff imposed → imports fell → trade balance improved → INR stabilized
- Lesson: trade balance improvements complement carry; static CA surplus/deficit is money-losing as standalone

**Mexico Taper Tantrum 2013**
- US 10Y moved from 1.80% to 3.18% (May-Sept 2013)
- Mexico 10Y moved from 5.25% to 7.21% — beta 1.4 (some days >3)
- Peak move divergence: US bottomed May 3, Mexico bottomed May 10
- Lesson: US rates bottoms and EM rates bottoms rarely coincide; front ends are not safe during rapid UST sell-offs

**Argentina El Cepo (2011-2015)**
- Severe capital controls created profitable NDF opportunity
- Blue swap rate volatility created total return opportunities; IMF-basis investors earned high carry
- Onshore-offshore spreads created pure arbitrage pre-2015 election
- Lesson: severe capital controls are untradable directionally, but onshore-offshore spread arbitrage can be profitable

---

## Contrarian and Non-Consensus Views

1. **Interest rate differentials are money-losing for EMFX** — the single most dangerous mistake G10 traders make in EM. Rising EM rates often coincide with weaker FX (inverse of G10).

2. **Simple carry has been broken since 2011** on USD funding. High EM yields ≠ profitable carry trades when DXY is in a structural uptrend.

3. **Current account strength is money-losing** as a standalone FX signal. Improvement in trade balances helps, but static CA surplus/deficit does not predict returns.

4. **US HY spreads are a better EM leading indicator than VIX.** Most EM investors monitor VIX; they should monitor US HY.

5. **NFP is noise for EMFX.** CPI and FOMC dominate; payrolls have no reliable follow-through.

6. **Positioning is a momentum signal, not contrarian.** Being long when the market is long is usually profitable; fading consensus loses money more often than it wins.

7. **Flows follow price, not the other way around.** Asia FX leads equity flows; using flows as a leading indicator is backwards.

8. **Linkers are structurally superior** to nominals on a risk-adjusted basis. Leverage linkers rather than holding nominals outright.

9. **Commodity exporters benefit from commodity rallies through FX strength** (lower tradables inflation), making them paradoxical receivers during global inflation scares.

10. **China's 1.9% August 2015 devaluation changed Fed policy** — the single most important EM event for global macro in the 2010s. S&P fell 10% in 4 days; Fed delayed the September hike.

11. **Equal-weighting and inverse-GDP-weighting beat cap-weighting** for EM indices. Market-cap indices reward debt issuance, not creditworthiness.

12. **EM ESG scores are unfair** without adjusting for development stage. CO2 per unit GDP must be regressed on GDP/capita to be meaningful.

---

## Limitations and Blind Spots

### What the Book Does Not Cover Well
- **Frontier FX** (only touched briefly in portfolio construction; no systematic FX strategies for frontier)
- **Options strategies** (mentioned as "weapons of mass alpha" but not developed; no vol surface analysis, no gamma/vega frameworks)
- **Intraday execution** (the book operates at daily/weekly/monthly horizons; no microstructure advice)
- **Sanctions and geopolitical tail risk** (pre-2022 Russia/Ukraine; framework would need significant updating)
- **Digital currencies and stablecoins** in EM context (not addressed)
- **EM corporate credit** (CEMBI mentioned but not deeply analyzed)

### What Has Changed Since Publication (2020)
- **Post-COVID EM rate cycle** was unprecedented in speed and magnitude; the book's cycle timing rules need recalibration for the 2020-2024 period
- **Fed hiking cycle of 2022-2023** (525bp) was the fastest since the 1980s; "benign Fed hiking" assumption may not hold
- **China structural slowdown** (property crisis, demographics) may weaken the China → commodity → EMFX transmission mechanism
- **Geopolitical fragmentation** (US-China decoupling, sanctions on Russia) has created new correlation regimes not present in the backtest sample
- **EM local markets have deepened significantly** since 2018 data cutoff; some liquidity assumptions may be stale

### Methodological Limitations
- Backtests end around 2018; all IRs and Sharpes should be treated as in-sample for post-2018 trading
- Many strategies have few observations in the tails (emergency hikes: 20 events; domestic disasters: 7 events; curve inversions: 6 events)
- The 65/35 split is a regression artifact — the actual split varies meaningfully over time (Table 2.2 shows it can shift)
- Chinese data quality issues acknowledged but not quantified
- Most backtests assume frictionless execution and no market impact; EM liquidity can be episodically terrible

### Author Biases
- **Citi desk perspective**: The authors write from a sell-side research / trading desk viewpoint; buy-side portfolio construction constraints (benchmark tracking, drawdown limits, committee governance) are addressed but not their primary lens
- **Latin America overweight**: Brazil receives disproportionate case study attention; Asia and Africa are thinner
- **Quantitative-empirical bias**: Strong preference for backtestable signals over qualitative political analysis; may underweight truly idiosyncratic political risk
