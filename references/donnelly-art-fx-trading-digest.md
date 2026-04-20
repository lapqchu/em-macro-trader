# Donnelly — The Art of Currency Trading: Method Digest

**Source**: Brent Donnelly, *The Art of Currency Trading: A Professional's Guide to the Foreign Exchange Market* (Wiley, 2019)
**Ingestion date**: 2026-04-20
**Digest scope**: Complete book (Chapters 1–16), all frameworks, quantitative parameters, and heuristics extracted

---

## 1. Core Thesis: The Fusion Approach

Donnelly's central claim is that sustainable FX profitability requires **fusion** — the convergence of five independent analytical branches:

1. **Fundamental / macro analysis** — what should the currency do given the economic regime?
2. **Technical analysis** — where are the structural price levels and what do momentum indicators say?
3. **Behavioral finance** — what biases are distorting market pricing, and what does sentiment/positioning imply?
4. **Correlation / intermarket analysis** — are related variables (rates, commodities, equities) confirming or diverging?
5. **Risk management** — does the trade fit within your capital, sizing, and stop-loss framework?

When all five branches point in the same direction, the result is a **Five-Star trade** — the highest-probability, highest-conviction setup. The discipline is to wait for these convergences rather than forcing trades from any single dimension.

**Method transfer**: This maps directly to our existing em-macro-trader architecture. Willer provides the tactical EM catalyst layer, Booth the strategic framework, James the optionality lens, Jha the rates mechanics. Donnelly now adds the practitioner-level FX execution philosophy — how to actually identify, enter, size, and manage trades once the macro/structural view is formed.

---

## 2. FX Driver Framework

### 2.1 Four Global Drivers

| Driver | Mechanism | Key Currencies Affected |
|---|---|---|
| **Global growth** | Strong global growth → exporters benefit (CNY, KRW, BRL); weak → safe haven flows (JPY, CHF, USD) | All, but EM most sensitive |
| **Commodity prices** | Commodity strength → exporter currencies up; importer currencies down | CAD, AUD, NZD, NOK, BRL, ZAR (exporters); TRY, INR (importers) |
| **Risk aversion** | Risk-off → low-yielders rally (JPY, CHF); high-yielders sell off (EM, AUD, NZD) | Universal — overrides domestic fundamentals in extreme episodes |
| **Geopolitics** | Country/regional risk triggers flight; can also trigger commodity dislocations | RUB, PLN, TRY, MXN (regional contagion); petrocurrencies (via oil) |

### 2.2 Three Domestic Drivers

| Driver | Key Principle |
|---|---|
| **Monetary policy** | Number-one domestic driver most of the time. *Changes in CB bias* are more important than the level of rates. By the time rates actually move, much is priced in. |
| **Capital flows** | FDI, M&A, portfolio flows. More important in EMFX than G10. Hard to predict; usually ex-post explanation. |
| **Trade balance / current account** | Long-run determinant with little short-run influence. Goes in/out of vogue; becomes critical during rising global/US rates as an indicator of financing pressure. |

### 2.3 Regime Identification

The market oscillates between focusing on global factors and domestic factors:
- **High risk aversion / intense China focus** → domestic drivers become irrelevant
- **Stable world** → domestic drivers dominate, global factors muted

**Key skill**: Identifying which regime you are in *right now*. This echoes Willer's regime-sensitivity framework and Booth's "65% global factor" — when global conditions dominate, EM idiosyncratic stories cannot overcome the macro headwind.

### 2.4 The Dollar Smile (Stephen Jen)

Three-state model for USD:
1. **USD strong**: US/global recession → risk aversion → safe haven USD buying
2. **USD weak**: US slow / global OK → sell dollars, buy risk
3. **USD strong**: Very strong US growth + hawkish Fed → capital attraction → buy USD

USD rallies *into* US recessions — counterintuitive but consistent. Mechanism: global trade financed in USD → fewer dollars in circulation globally → USD shortage → dollar up. Donnelly's caveat: empirical evidence is mixed; treat as heuristic, not law.

**Cross-reference with Booth**: The Dollar Smile complements Booth's EM structural framework — State 1 and 3 are both hostile to EM (risk-off or US exceptionalism), State 2 is the EM sweet spot.

---

## 3. The Critical Concept: Delta vs. Level

**The market trades off the change, not the level of fundamentals.**

- A country with poor but *improving* fundamentals will see currency appreciate vs. a country with great but *worsening* fundamentals.
- Prices are set at the margin; widely known information is already in the price.
- The most important aspect of new information: whether it is strong or weak **relative to market expectations**, not relative to history.

This is the single most important fundamental concept in Donnelly's framework and applies universally — DM and EM.

**Cross-reference with Willer**: This is the analytical backbone of Willer's catalyst-based approach. Willer's tactical signals are delta-driven — what is changing at the margin, not what the absolute level of an indicator is.

---

## 4. Interest Rate Framework

| Condition | Currency Effect |
|---|---|
| High rates | Bullish |
| Rising rates | Bullish |
| Steep yield curve | Bullish (accommodative CB + good growth outlook) |
| Steepening curve | Bullish |
| Inverted curve | Precedes recession → bearish medium-term |

**Inflation regime matrix** (critical for EM):

| Regime | Currency Effect |
|---|---|
| Rising inflation + credible hawkish CB (typical G10) | Bullish — CB will hike |
| Rising inflation + CB behind the curve | Bearish — real rates falling |
| Falling inflation/deflation + impotent CB | Can be bullish (Japan pre-2012) |
| Falling inflation + credible easing CB | Bearish — CB will cut |

**EM-specific warning**: Foreigners buy/sell bonds currency-hedged; high inflation can trigger either bond liquidation (sell currency) or attract yield seekers (buy currency). Outcome depends on existing positioning. Donnelly's rule: stay away from trading EM currencies after inflation data releases — moves often confusing and random.

**Cross-reference with Jha**: Jha's rates mechanics framework (DV01, carry decomposition, forward rates) provides the technical precision behind Donnelly's higher-level interest rate intuition.

---

## 5. Technical Analysis: Practitioner Philosophy

### 5.1 Core Principle

**TA is best used as a risk management and tactical tool, NOT a trade selection or forecasting tool.** Never do a trade just because a chart looks good. Come up with ideas elsewhere (macro, positioning, cross-asset), then use TA to determine entry, stop loss, take profit, and position size.

### 5.2 Preferred Setup

- Moving averages: **20, 55, 100, 200-period** on 10-minute and 1-hour charts
- Best single MA: **200-hour**
- Momentum: MACD, RSI, Parabolic SAR, and the Deviation (Setup 3 below)
- Charting: Candlesticks primary, Market Profile secondary

### 5.3 Regime Identification

- **Trending markets**: Where the big profits come from. Only follow trends if you believe in the reasoning *beyond the chart*. Trade pullbacks to MA (preferred) or breakouts with 1.5× ADR stop.
- **Rangebound markets**: Most difficult. Buy near bottom, sell near top. Positioning matters more.

### 5.4 Key Rules

- **Rule #4**: If you look hard enough, you can always find a tech level to justify a bad trade.
- **Rule #5**: "It's a big level" is not a good enough reason to put on a trade.
- **Convergence**: When multiple technical indicators (MA + support + round number + trendline) converge near a single level → much stronger signal.

---

## 6. The Seven Deadly Setups

### Setup 1: Slingshot Reversal
**Definition**: An important S/R level breaks temporarily then reverses back into the old range. Massive positioning builds on the broken side; when it fails, the squeeze is violent.
**Entry**: Stop entry 10bp (0.10%) inside the recaptured level.
**Stop**: 10bp beyond the new extreme.
**Target**: 1.5–2× ADR or next major S/R.

### Setup 2: Shooting Stars and Hammers
**Purpose**: Clear reversal signal when you have a countertrend view but need the market to confirm exhaustion.
**Entry**: Close of the hammer candle.
**Stop**: Below/above the hammer's extreme wick.
**Combo**: Slingshot + Hammer together = especially powerful.

### Setup 3: Extreme Deviation from 100-Hour MA (The Deviation)
**Threshold**: >1% deviation from the 100-hour MA signals overextension.
**Stop**: Additional 0.7% away from entry.
**Caveat**: Only fade when there is no strong fundamental justification for the move.
**Best pair**: USDCAD (known mean reverter).
**Secondary use**: Take-profit indicator on winning trades (deviation >100 pips → sell some).

### Setup 4: Volume Spike at a Price Extreme
**Concept**: High volume at a price extreme = capitulation, risk transferring from weak to strong hands.
**Entry**: Wait 2–3 bars (60–90 min on 30-min chart) of declining volume after the spike.
**Stop**: Beyond the extreme.
**Target**: Top of the waterfall (pre-crash level).

### Setup 5: Broken Triangles
**Definition**: Triangle breaks one direction, fails, reverses through the other side. Same concept as Slingshot but specific to triangle formations.
**Entry**: When price closes back inside the triangle on the reversal.
**Stop**: Outside the broken side.
**Frequency**: Rare but extremely powerful.

### Setup 6: Double/Triple Top/Bottom
**Entry**: Sell near multiple tops (buy near multiple bottoms) with very tight stop just beyond.
**Key advantage**: Tight stop → large leveraged position → small percentage risk, large notional opportunity.

### Setup 7: Sunday Gaps
**Pattern**: Major weekend news → gap at Sunday open → **85% fully reverse within 48 hours**.
**Entry**: Take the other side of the gap in the opening hour.
**Stop**: One ADR away.
**Take profit**: When gap is 90% filled.
**Warning**: "Double black diamond" — psychologically the hardest trade, which is precisely why it works.

### Multi-Setup Convergence → Five-Star Technical

Multiple setups occurring simultaneously (e.g., Slingshot + Volume Spike + Deviation all at once) = "triple play." The more concurrent setups, the higher conviction. Add macro reasons on top = time for maximum position size.

**Crosswinds rule**: When bullish and bearish indicators are roughly equal → pass on the trade entirely. Do not ignore contradictory evidence.

---

## 7. Correlation and Intermarket Trading

### 7.1 Correlation Validity Checklist

Before trusting any correlation:
1. Does it make econometric/logical sense?
2. Is the correlation likely to persist?
3. Are there periods of both rising and falling prices in the sample?
4. What third variables might be driving both?

### 7.2 Reliability Ranking

1. FX vs. other currencies
2. FX vs. interest rates
3. FX vs. commodities (gold, oil, copper)
4. FX vs. equity indices
5. FX vs. single-name equities and ETFs

### 7.3 Currency Driver Map (13 pairs)

| Currency | Driver 1 | Driver 2 | Driver 3 | Driver 4 |
|---|---|---|---|---|
| USD | US 2/5/10y rates | US equities | Gold | ISM / confidence |
| EURUSD | US/DE rate diff | Gold | Italy 2y/10y | Crude oil |
| USDJPY | Nikkei | US 2/5/10y | Gold | S&P |
| USDCHF | US 2/5/10y | Gold | — | — |
| EURCHF | DE rates | Global risk appetite | — | — |
| GBPUSD | UK/US rate diff | Crude oil | — | — |
| EURGBP | DE/UK rate diff | — | — | — |
| AUDUSD | AU/US rate diff | Gold | Copper/iron ore | BHP, FCX, FXI |
| AUDNZD | AU/NZ rate diff | AU vs NZ equity ratio | — | — |
| NZDUSD | NZ/US rate diff | Dairy (MMRA) | — | — |
| USDCAD | Crude oil | US/CA rate diff | CA oil equities | Gold |
| EURNOK | Crude oil | DE/NO rate diff | — | — |
| EURSEK | DE/SE rate diff | OMX | — | — |

### 7.4 The Lead/Lag Method

1. Create 50–60 overlay charts (each major pair vs. its key drivers)
2. Hourly charts scaled to 21–42 days (1–2 months of data)
3. Scan for divergences each morning
4. When divergence found: check other drivers for the same currency → do they confirm?
5. Multiple variables aligned + FX hasn't responded = trade opportunity
6. Avoid crosswinds — only trade when strong winds at your back

**Decision rule for divergences**: The variable with the most momentum wins. If copper breaks out and AUD hasn't moved → long AUD. If AUD breaks higher and copper hasn't → do nothing.

### 7.5 FX vs. Equity Regime Awareness

The equity-FX correlation **can flip direction**:
- Late 1990s: US equities up = USD up (capital inflows to US tech)
- 2003–2010: US equities up = USD down (RORO regime)
- Post-2012: US equities up = USD up (US outperformance)

**Critical**: Know what regime you are in. Do not assume stable correlations.

---

## 8. Behavioral Finance and Sentiment

### 8.1 Positioning vs. Sentiment — Critical Distinction

- **Sentiment** = how people *view* the market (surveys, DSI)
- **Positioning** = actual positions held (COT, bank data)
- They are NOT the same. When they diverge, it creates the most important trading signals.

### 8.2 Six States of Sentiment

| State | Signal |
|---|---|
| High and stable | Bullish |
| High and rising | Very bullish |
| High but *falling* | **BEARISH** (contrarian) |
| Low and stable | Bearish |
| Low and falling | Very bearish |
| Low but *rising* | **BULLISH** (contrarian) |

The contrarian signals come when sentiment diverges from price action.

### 8.3 COT Positioning Decision Rules

1. Positions and price normally trend together
2. Positioning often *leads* price at turning points — watch for divergence as early warning
3. Rate of change matters more than absolute level
4. **Never sell just because "the market's long"** — usually just means strong trend
5. Most profitable to go WITH COT positioning, not against it

### 8.4 Nine Cognitive Biases with FX Countermeasures

| Bias | FX Manifestation | Countermeasure |
|---|---|---|
| **Confirmation** | Cherry-picking data details; chart-shopping | Get flat — only when flat can you process information unbiased |
| **Overconfidence** | Oversizing; blindness to weaknesses | Consider alternative hypotheses |
| **Extrapolation / Recency** | Forecasts = spot × 1.08; assumes current trend continues | Independent thinking; be wary if theme has run 6 months |
| **Asymmetric loss aversion** | Can't exit losers; loss feels 2× as bad as equivalent gain | Reframe: "Good, another small loss — sticking to plan" |
| **Greed and fear** | Feedback loops; FX overshooting on all timeframes | Small positions when fading extreme emotion; use volume spikes to identify peaks |
| **Anchoring** | Waiting to get back to entry before exiting | If view changes, exit immediately regardless of entry |
| **Round number** | Orders cluster on 00/50; highs/lows cluster on rounds | Bid at 01/03, sell at 97/99; stop below 00 not above |
| **Favorite/longshot** | Chasing 5–10% moves; ignoring routine 50–70bp daily moves | Focus on high-EV routine trades, not home runs |
| **Herding** | Economists cluster around mean; career risk dominates | Economic surprises happen more often than forecasts suggest |

### 8.5 Anecdotal Indicators

- **Magazine Cover Indicator**: Theme on mainstream covers → trend near exhaustion (~68% reverse indicator one year later). Timing imprecise.
- **Cheer Hedge**: When a trader celebrates a winning position → immediate reversal. Self-application: counting P&L before bed → cut 30–50% immediately.
- **WTF Indicator**: When many people ask "WTF?" about a move → the move has further to run. Those asking are on the wrong side.
- **IPO Indicator**: Massive IPO → potential top in that industry/market. Glencore IPO (2011) = exact CRB commodity top.

---

## 9. News Trading Framework

### 9.1 The NewsPivot Concept

**NewsPivot** = the price level immediately before a news release. Critical reference point:
- Good news + currency falls back through NewsPivot → bearish (good news / bad price)
- Bad news + currency rallies back through NewsPivot → bullish (bad news / good price)
- Stop losses on news trades: ~10 pips above/below the NewsPivot

### 9.2 Three Data Trading Strategies

| Strategy | When to Use | Entry |
|---|---|---|
| **Go with extreme data** | Number >2σ miss/beat; market positioned wrong way | After first algo wave, on the brief consolidation/bounce |
| **Fade the kneejerk** | Headline strong but details weak (or vice versa) | Take other side of the initial algo-driven move |
| **Bad news / good price** | Price reverses after unambiguous news for no macro reason | Follow the price, not the news |

**Meta-rule**: Only thing that matters is actual vs. expectations. Not vs. last month. The whisper number (what the market *actually* expects) can differ from economist consensus — whisper matters more.

### 9.3 Central Bank Meeting EV Framework

1. Need a view that *differs* from market pricing — if you agree with market odds, nothing to do
2. Construct EV grid: assign probabilities to each outcome, estimate spot levels, calculate weighted payoff
3. Check where breakeven probability is
4. **Rule #9**: Never fade unexpected CB moves — jump on them, be fast and aggressive
5. Unscheduled CB actions = always a "go with"

### 9.4 Correlated News Plays

Trade FX as proxy for correlated asset events:
- OPEC meeting → trade USDCAD
- DoE inventory data → USDCAD
- NZ milk auctions → NZDUSD

Profitable because the market may not be ready to trade the correlated FX pair as quickly as the primary asset.

**Sympathy plays**: Global CBs often move in the same direction — one cutting increases probability of others cutting (e.g., BOC cut Jan 2015 → traders immediately sold AUDUSD).

---

## 10. Risk Management System

### 10.1 Free Capital

Free capital = how much you can **afford to lose**. Not total capital, not leveraged capital.
- Retail: account balance
- Hedge fund: capital × max drawdown clause
- Free capital + P&L targets = the two support beams of all risk management

### 10.2 Monthly Chunking

Manage risk on a **monthly** basis:
1. Monthly stop loss = **10% of adjusted free capital** (initial + YTD P&L)
2. Monthly target = **2× monthly stop loss**
3. Hit stop → stop trading completely, wait for calendar reset
4. Hit target → slow down, protect, don't stop
5. System automatically increases risk when winning, decreases when losing

### 10.3 Conviction-Based Position Sizing

| Conviction | % of Adjusted Free Capital at Risk |
|---|---|
| Three-Star | 1% |
| Four-Star | 3% |
| Five-Star | 6% |

- Never more than **8% of free capital at risk** across all positions at any time
- Size high-conviction trades **3–4×** low-conviction trades
- Rarely more than 3–4 trades simultaneously; often just one

### 10.4 Position Size Formula

```
POSITION SIZE = ($ AT RISK) / (LOSS PER UNIT IF STOP TRIGGERS)
```

Position size is **always** determined by stop location, never the other way around.

### 10.5 Kelly Criterion

```
% of Capital = Win% − ((1 − Win%) / (Avg Win / Avg Loss))
```

**Use half-Kelly or quarter-Kelly** to compensate for the fact that in trading (unlike gambling) probability of winning is estimated, not known, and multiple bets may be simultaneous.

### 10.6 Stop Loss Rules

**Three placement techniques (combine):**
1. **Technical convergence** + 20% of daily range as buffer
2. **ADR-based**: Short-term = entry ± 1.2× ADR; Medium-term = entry ± 2.5× ADR
3. **Trailing**: Use 100-hour MA + buffer, updated every 12–24 hours

**Three iron rules:**
1. Write the stop down before or immediately after entry
2. Do NOT move it (exceptions: trailing to lock profit, upcoming event risk)
3. Automate the execution

**If stopped out**: 4-hour cooling-off period before re-entering the same trade.

### 10.7 Take Profit

- Use technical levels (next resistance, prior highs)
- Err on conservative side (bid at 01/11 above round, not at the round)
- Risk/reward is two-dimensional: distance AND probability
- EV = (pips reward × P(TP)) − (pips risk × P(SL))

---

## 11. Trade Management and Psychology

### 11.1 Tight/Aggressive Wins (Rule #22)

Don't be involved in many trades, but when involved, be as aggressive as possible. Wait, wait, wait — then when everything lines up, pounce.

### 11.2 Gut vs. Head Framework

- **Head and gut aligned** → maximum conviction, maximum size
- **All head, no gut** → investigate: is gut seeing a pattern from experience, or just fear?
- **All gut, no head** → danger of confirmation bias; seek contradicting evidence
- **Head and gut conflict** → do more work, or do nothing

### 11.3 Slump Protocol

1. Square all positions
2. Cut to **20% of normal size** for a few days
3. Talk about the slump (peers, boss, psychologist)
4. Use the time for research and reading
5. Get perspective — wait for next high-conviction Five-Star to re-engage

**Probabilistic reality**: A 55% winner averages 2–3 five-day losing streaks per year.

### 11.4 Overtrading Prevention

Three methods:
1. **Trade quota** — max N trades per day/week
2. **Time windows** — only enter/exit at designated times (e.g., 7AM NY and 11AM NY)
3. **Extreme position size variation** (Donnelly's personal method) — 1 unit dabbling to stay in feel, 5–20 units on Five-Star

### 11.5 Process vs. Outcome Matrix

| | Good Outcome | Bad Outcome |
|---|---|---|
| **Good Decision** | Reinforces process | Disappointing but fine — do not respond emotionally |
| **Bad Decision** | Lucky — will lead to more bad process | Learn from it. Same mistake repeatedly? |

With 55% win rate: P(profit today) = 55%; P(profit this week) ≈ 60%; P(profit this month) ≈ 75%; P(profit this year) > 90%.

---

## 12. Market Microstructure

### 12.1 Time-of-Day Framework

**LDN/NY overlap (7AM–12PM NY)** = >50% of daily FX volume in only 25% of hours. This is where you make money.

Key daily events (EST):
- 2:00 AM — London open (inflection point)
- 7:00 AM — NY open (overlap begins)
- 8:30 AM — Most US data
- 10:00 AM — Option expiry + 2nd-tier data
- 11:00 AM — WMR fix (5-min window; massive volume)
- 3:00 PM — CME close
- 5:00 PM — NY close / roll time
- **5:00–6:00 PM — Twilight Zone**: worst liquidity of the day, do NOT trade

**Donnelly's P&L pattern**: Made money 7–11AM NY; gave back 20–40% in the afternoon. Action: actively trade the overlap, step away during quiet periods.

### 12.2 WMR Fix

- 5-minute window (10:57:30–11:02:30 NY)
- Real money uses WMR to value foreign holdings → enormous volumes converge
- When everyone is the same direction at the fix → outsized moves
- Opportunity: if a currency gets crushed into the fix and you had prior bullish reasons, the fix provides a great entry (reversals common after 11:02:30)
- **Month-end fix** is by far the largest — equity fund FX rebalancing

### 12.3 Cross-Pair Vol-Weighting Rule

When trading non-USD crosses, the higher-beta (more volatile) leg dominates:
- CADMXN ≈ USDMXN trade (ρ = 0.76 to USDMXN, ρ = −0.10 to USDCAD)
- AUDCAD ≈ AUDUSD trade

**Solution**: Vol-weighted combo instead of outright cross. E.g., instead of 130 CADMXN, do long 75 USDMXN + short 100 USDCAD.

### 12.4 Currency Basket Approach

When you have a view on one currency but no strong view on the other side → trade against a basket. Avoids idiosyncratic risk in the non-USD leg. Higher capacity for large positions.

---

## 13. US Economic Data — Trader's Guide

### Key Releases (Ranked)

| Release | Stars | Key Notes |
|---|---|---|
| Nonfarm Payrolls | 5 | First Friday; avg miss 72.2K, 1σ = 83.6K; avg USDJPY 5-min range 66 pips |
| GDP (Advance) | 5 | Quarterly; avg miss 0.35%; trade Advance only |
| ISM Mfg + Non-Mfg | 4 | First business day; New Orders most forward-looking |
| Consumer Confidence | 3.5 | Leading indicator |
| Retail Sales | 3.5 | Focus on MoM ex-autos and gas |
| Initial Claims | 3 | Weekly; most timely indicator |
| CPI | 3 | Importance surges above 2% |
| Durable Goods | 3 | Ignore headline; focus on MoM ex-transportation |
| Regional PMIs | 3 | Chicago PMI: subscribers get it at 9:42, public at 9:45 |

### Meta-Rules for Data Trading

- Only thing that matters: actual vs. expectations (not vs. prior)
- When multiple time periods released simultaneously, shorter period (MoM) is always most important
- Three criteria for data importance: **timeliness, relevance, reliability**
- Economists cluster around the mean (career risk) → actual data far more volatile than forecasts suggest

---

## 14. Quantitative Parameters Reference Table

| Parameter | Value |
|---|---|
| Slingshot entry offset from key level | 10bp (0.10%) |
| Slingshot stop from new extreme | 10bp |
| Slingshot take profit | 1.5–2× ADR or next major S/R |
| Deviation threshold (100-hour MA) | >1% of spot |
| Deviation stop buffer | +0.7% beyond entry |
| Volume spike entry wait | 2–3 bars (60–90 min on 30-min chart) |
| Breakout stop loss | ~1.5× ADR |
| Flag target | Flagpole length added to flag boundaries |
| Sunday Gap reversal rate | 85% fill within 48 hours |
| Sunday Gap stop | 1× ADR |
| Sunday Gap take profit | 90% of gap |
| Preferred MAs | 20, 55, 100, 200-period |
| Best single MA | 200-hour |
| RSI thresholds | 30 / 70 |
| Monthly stop loss | 10% of adjusted free capital |
| Monthly target | 2× monthly stop |
| 3-Star position risk | 1% of adjusted free capital |
| 4-Star position risk | 3% of adjusted free capital |
| 5-Star position risk | 6% of adjusted free capital |
| Max total risk at any time | 8% of free capital |
| High-conviction vs. low-conviction size ratio | 3–4× |
| Stop loss ADR buffer (short-term) | 1.2× ADR |
| Stop loss ADR buffer (medium-term) | 2.5× ADR |
| Tech stop buffer | Level + 20% of daily range |
| Post-stop cooling off | 4 hours |
| Good trader win rate range | 50–60% |
| Slump size reduction | 20% of normal |
| NFP average miss | 72,200 |
| NFP 1σ miss | 83,600 |
| NFP avg USDJPY 5-min range | 66 pips |
| GDP Advance avg miss | 0.35% |
| Kelly application | Half-Kelly or quarter-Kelly |

---

## 15. Donnelly's 25 Rules of FX Trading

1. Don't blow up. Avoid risk of ruin above all else.
2. Adapt or die.
3. Do the work. Read the speeches. Analyze, read, and study.
4. If you look hard enough, you can always find a tech level to justify a bad trade.
5. "It's a big level" is not a good enough reason to put on a trade.
6. No mo' FOMO. Never worry about missing it.
7. Flat is the strongest position. When in doubt, get out.
8. It doesn't always have to make sense.
9. Never fade unexpected CB moves. Jump on them.
10. Making money is hard. Keeping it is harder.
11. Successful traders make more money on up days than they lose on down days.
12. Anything can happen.
13. Keep a trading journal.
14. There is a time and a place to go big.
15. Good traders vary bet size.
16. It always looks bid at the highs. It always looks heavy at the lows.
17. You control the process but you do not control the outcome.
18. Each trade is a drop of water. The market is an ocean.
19. Know your edge.
20. Know your time horizon.
21. Good traders have a plan.
22. Tight/Aggressive wins.
23. Be flexible. Don't get married to a view.
24. Do not let random, low-conviction trades kill you.
25. Have fun. If you don't enjoy it, what's the point?

---

## 16. Cross-References with Existing Architecture

| Donnelly Concept | Existing Source | Integration Note |
|---|---|---|
| Delta vs. Level | Willer (catalyst-driven tactical signals) | Donnelly provides the theoretical foundation; Willer operationalizes it for EM specifically |
| Dollar Smile (USD regime) | Booth (65% global factor; DXY as EM headwind) | State 1 and 3 = hostile to EM; State 2 = EM sweet spot |
| Interest rate framework | Jha (DV01, carry, forward rates, curve analysis) | Donnelly gives the macro intuition; Jha provides the rates mechanics to structure trades |
| FX driver map (13 pairs) | Willer (EM-specific driver tables) | Donnelly covers DM pairs + cross-pair construction; extends the toolkit beyond EM |
| Seven Deadly Setups | James (gamma, barrier, optionality) | James provides the options overlay for entries near Donnelly's technical levels |
| Conviction sizing (1/3/6%) | Jha (position sizing via DV01) | Donnelly's framework applies to FX notional; Jha's applies to rates risk. Same principle: size to conviction and volatility |
| CB meeting EV framework | Willer (CB catalyst framework) | Donnelly quantifies the EV; Willer identifies the EM-specific CB dynamics |
| Correlation / intermarket | Booth (global factor model) | Donnelly's lead/lag method is the tactical execution layer for Booth's strategic correlation insights |
| Free capital / monthly chunking | None (new) | First systematic P&L / drawdown management framework in the architecture |
| Behavioral biases + sentiment | None (new) | First formal behavioral finance layer; complements all existing sources |
| News trading (NewsPivot, 3 strategies) | None (new) | First systematic data/event trading framework |
| Slump protocol + overtrading prevention | None (new) | First systematic trade management psychology framework |

---

## 17. Method Transfer Notes

### What Donnelly Adds to the Architecture

1. **DM FX analytical depth**: The existing architecture was EM-focused. Donnelly provides the DM FX layer (G10 driver maps, cross-pair construction, correlation trading) that is essential because DXY views inform EM positions via the 65% global factor.

2. **Practitioner execution framework**: Willer/Booth/James/Jha are primarily about *what* to trade and *why*. Donnelly is about *how* — entry timing, stop placement, position sizing, conviction grading, and trade management.

3. **Behavioral self-management**: The nine cognitive biases with specific countermeasures, anecdotal indicators, slump protocol, and overtrading prevention methods are entirely new to the architecture.

4. **Risk management system**: Monthly chunking (10% stop / 2× target), conviction-based sizing (1/3/6%), Kelly criterion application (half/quarter-Kelly), and the free capital concept provide a complete P&L management framework.

5. **News/data trading**: The NewsPivot concept, three data strategies, and CB meeting EV grid are systematic approaches to event-driven FX trading not covered by other sources.

### How to Apply

- **Before any FX trade**: Run through Donnelly's Five-Star checklist (fundamentals + cross-market + positioning + technicals + gut) alongside the existing Willer/Booth/James/Jha layers
- **For entry timing**: Use the Seven Deadly Setups and the lead/lag divergence method
- **For sizing**: Apply the conviction-based framework (1/3/6%) within the monthly chunking system
- **For DM FX legs of EM trades**: Use the currency driver map and correlation framework
- **For self-management**: Monitor for the nine biases, apply the slump protocol when needed, track P&L OHLC daily
