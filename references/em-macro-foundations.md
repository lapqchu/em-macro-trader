# EM Macro Foundations — Core Knowledge Base

This document serves as the foundational reference for the EM macro trading skill. It contains baseline institutional knowledge, analytical frameworks, and market conventions that inform all responses. It is supplemented by digests of specific books and papers stored in this directory.

---

## 1. EM FX — First Principles

### What Drives EM Currencies

EM FX is ultimately about capital flows, and capital flows are driven by the interaction of:

**Pull factors** (domestic):
- Real interest rate differentials (the carry motive)
- Growth differentials (the equity/FDI motive)
- Institutional quality and rule of law (the structural allocation motive)
- Current account surplus/deficit (the fundamental anchor)

**Push factors** (external):
- US monetary policy and dollar liquidity conditions
- Global risk appetite (VIX, credit spreads, funding conditions)
- Commodity prices (for commodity-sensitive EM)
- Geopolitical regime shifts

The relative importance of pull vs. push factors varies over time. In risk-off environments, push factors dominate and country differentiation collapses. In benign environments, pull factors reassert and dispersion increases.

### The Balance of Payments as Anchor

The single most important macro framework for EM FX is the balance of payments. Not the current account alone — the full BoP including the financial account.

Key principles:
- A current account deficit is not inherently bearish for FX if it is financed by stable capital (FDI, long-term portfolio flows). It is bearish when financed by short-term hot money.
- The quality of financing matters more than the headline deficit.
- Reserve accumulation (basic balance surplus) is a cleaner signal than current account alone.
- Basic balance = current account + net FDI. This is the structural anchor.

### Real Effective Exchange Rate (REER)

REER is a useful but dangerous metric:
- It tells you about valuation, not timing.
- An "overvalued" currency can stay overvalued for years if capital flows support it.
- REER models depend heavily on the base period, the deflator (CPI vs. PPI vs. ULC), and the trade weight methodology.
- Never use REER as a standalone trade signal. Use it as context for a flow-based thesis.

---

## 2. EM Rates — First Principles

### Local Currency Rates

The local curve is driven by:
- Central bank policy rate (the anchor for the front end)
- Inflation expectations (the driver of the belly and long end)
- Fiscal risk premium (the driver of the long end and term premium)
- Foreign positioning (can cause technical distortions, especially in liquid markets like MXN, ZAR, BRL)
- Supply dynamics (issuance calendar, buybacks, switches)

### Key Analytical Distinction: Nominal vs. Real Rates

Always think in real terms. A 10% nominal yield in a country with 9% inflation is not "high yields" — it is a 1% real rate. Compare:
- Ex-ante real rate (nominal minus inflation expectations)
- Ex-post real rate (nominal minus realized inflation)
- Neutral real rate (model-dependent, but essential for assessing policy stance)

### Hard Currency (External Debt)

Hard currency EM bonds are a hybrid asset:
- Duration risk (US Treasury component)
- Credit risk (sovereign spread component)
- The two are often negatively correlated in benign environments (spread tightening + Treasury rally) and positively correlated in stress (spread widening + Treasury rally as flight to quality)

Spread analysis should consider:
- Debt/GDP and debt trajectory
- External financing requirements
- FX reserve adequacy
- IMF program status and conditionality
- Index inclusion and benchmark effects

---

## 3. Market Conventions and Traps

### FX Conventions by Market

| Currency | Quotation | NDF/Deliverable | Key Convention Notes |
|----------|-----------|-----------------|---------------------|
| BRL | USD/BRL | Deliverable (onshore), NDF (offshore) | Ptax fixing, bus/252 day count for rates |
| MXN | USD/MXN | Deliverable | 28-day TIIE swaps |
| ZAR | USD/ZAR | Deliverable | JIBAR, 3m NACS convention |
| TRY | USD/TRY | Deliverable but limited liquidity | Lira swaps often quoted vs. SOFR |
| INR | USD/INR | NDF (offshore) | RBI intervention is structural, not just tactical |
| CNY/CNH | USD/CNY (onshore), USD/CNH (offshore) | CNY = onshore, CNH = offshore deliverable | PBoC fixing, CNY-CNH basis matters |
| IDR | USD/IDR | NDF (offshore) | Jakarta fixing (JISDOR) |
| KRW | USD/KRW | NDF (offshore) | Seoul fixing |
| PLN | EUR/PLN | Deliverable | Quoted against EUR, not USD |
| CZK | EUR/CZK | Deliverable | Quoted against EUR |
| HUF | EUR/HUF | Deliverable | Quoted against EUR |
| CLP | USD/CLP | NDF | |
| COP | USD/COP | NDF | |
| PEN | USD/PEN | NDF | |
| PHP | USD/PHP | NDF | |
| EGP | USD/EGP | NDF | Multiple exchange rate risk |
| NGN | USD/NGN | NDF | Parallel market premium |

### Common Traps

- **Confusing onshore and offshore rates**: CNY vs CNH, INR onshore vs NDF — these can trade at different levels, especially during stress.
- **Ignoring NDF fixing risk**: NDF settlement depends on the fixing rate, which can be manipulated or set under illiquid conditions.
- **Carry calculation errors**: Using spot-forward differential vs. clean interest rate differential vs. actual funding cost — these differ, especially when cross-currency basis is non-zero.
- **Day count mismatches**: Brazilian DI futures use bus/252; most others use ACT/360 or ACT/365. Comparing yields without adjusting for day count is a common error.
- **Index effects**: JP Morgan GBI-EM, EMBI, CEMBI rebalancing and inclusion/exclusion events can move markets independently of fundamentals.

---

## 4. Crisis Recognition Frameworks

### Early Warning Indicators

Not all of these need to be present, but clusters matter:

**External vulnerability**:
- Current account deficit > 4% of GDP and widening
- Short-term external debt > FX reserves
- Reserve coverage < 3 months of imports (or < 100% of short-term debt)
- Declining reserves trajectory

**Domestic overheating**:
- Credit-to-GDP gap positive and expanding
- Real estate price acceleration
- Real exchange rate appreciation > 2 standard deviations from mean
- Current account deterioration driven by consumption, not investment

**Policy credibility erosion**:
- Central bank losing independence (political appointments, mandate changes)
- Fiscal dominance signals (central bank financing government directly or indirectly)
- Capital controls imposed or threatened
- Multiple exchange rate regimes emerging

**Market signals**:
- CDS curve inversion (short-dated CDS > long-dated)
- FX vol term structure inversion
- Persistent forward premium above interest rate differential (devaluation expectations)
- Local bond market losing foreign participation rapidly

### Crisis Taxonomy

Not all EM crises are the same. The type determines the trade:

1. **Balance of payments crisis** (classic EM crisis): Current account deficit + insufficient reserves + sudden stop. Trade: short FX, short local rates initially then long after overshoot.
2. **Fiscal/debt crisis**: Government debt trajectory unsustainable. Trade: short hard currency bonds (CDS), FX may or may not weaken depending on financing structure.
3. **Banking crisis**: Private sector balance sheet problem that becomes sovereign. Trade: short FX, short bank bonds, potentially long sovereign CDS if banking sector is large relative to fiscal capacity.
4. **Political crisis**: Regime change, institutional breakdown. Trade: highly path-dependent, typically short FX + long vol.

---

## 5. Ingested Sources Index

*This section is updated each time a new source is ingested into the knowledge base.*

| Source | Date Ingested | Key Contribution |
|--------|--------------|-----------------|
| Willer, Chandran & Lam — *Trading Fixed Income and FX in EM* (2020) | 2026-04-16 | Core tactical framework: 65/35 global-local split, factor hierarchy (carry/momentum/growth surprises/valuation), rate cycle timing rules, event playbooks, credit sweet spots, portfolio construction. Full digest: `willer-chandran-lam-digest.md`. Checklists: `willer-checklists.md`. |
| Jerome Booth — *Emerging Markets in an Upside Down World* (2014) | 2026-04-20 | Core strategic framework: risk perception inversion (EM risk priced, DM risk ignored), four-dimensional risk assessment (SDm/Pr/U/E matrix), investor base structure as primary risk variable, three blow-up indicators, three-layer sovereign risk, market segmentation model, meme lifecycle analysis, GDP-weighted allocation logic, financial repression dynamics, Kübler-Ross fiscal crisis model. Full digest: `booth-upside-down-digest.md`. Checklists: `booth-checklists.md`. |
| James, Fullwood & Billington — *FX Option Performance* (2015) | 2026-04-20 | Options layer: empirical payoff/premium analysis across 34 pairs (20 EM) and 7 tenors. Core findings: EM puts systematically cheap at 3M+ (124% payoff/premium at 12M), EM calls systematically expensive (52% at 12M), OTM options overpriced vs ATMF, options dominate forwards for EM depreciation hedging, vol risk premium larger in EM than G10. Trading strategies: long-dated put buying (+10.3% ann. for USDBRL), carry-directed option trading, short-dated call selling (with tail-risk warnings). Full digest: `james-fx-options-digest.md`. Checklists: `james-fx-options-checklists.md`. |
| Jha — *Interest Rate Markets: A Practical Approach to Fixed Income* (2011) | 2026-04-20 | Rates mechanics layer: comprehensive DM rates plumbing that underpins the global regime driving 65% of EM returns. Core content: DV01-based risk thinking, carry + rolldown decomposition, forward rate mechanics, curve construction, Fed regime dynamics (easing/tightening/on-hold), Treasury supply/demand framework (total duration supply, demand by source — foreign CBs 50%, Fed, banks, pensions, funds), MBS convexity hedging positive-feedback loops, swap spread drivers and directionality, interest rate options (normal vs Black, Greeks, structural supply/demand for vol), Treasury futures basis/CTD/rolls, RV trade construction (regression-based butterfly weights, par curve analysis), carry-efficient directional trades, conditional curve and spread trades via swaptions. Method transfer: decompose every position into direction + carry + roll + vol + correlation + liquidity; specificity improves Sharpe; know your flows; forwards are poor predictors; beta instability kills RV trades. Full digest: `jha-rates-mechanics-digest.md`. Checklists: `jha-rates-mechanics-checklists.md`. |
| Donnelly — *Alpha Trader* (2021) | 2026-04-21 | Psychology, methodology, and mathematics layer (complements Art of Currency Trading): Alpha Trader equation (rational + intelligent + skilled + conscientious + calibrated confidence), 7-stage narrative cycle for strategic timing (narrative turns before price = most profitable moments), evolved Type I/II/III conviction system with YTD-adjusted sizing formula (Type II = 3% free capital + 10% YTD P&L → call-option P&L structure), Analysis of Competing Hypotheses (ACH) from CIA intelligence analysis, extended behavioral finance (grizzly bias, squirrel-chasing, outcome bias, apophenia with 4-step validation), risk appetite scoring (1-10 + three distorting effects), crisis market rules (VIX >40 overrides normal indicators), strategy decay detection (crowding mechanism + personal case study), variance vs. bad process 9-item diagnostic, self-management systems (Daily Sheet with mood/opportunity → risk budget formula, 12-12 journaling for accountability, One Goal system, DMN awareness, emotion management protocol with time delay), specific tradeable patterns (Turnaround Tuesday +4.3%, September seasonal, bubble deflation at ~85%, month-end dollar effect, run-up trade, "Everybody's Bearish Nobody's Short"). Method transfer: Alpha Trader adds the *when* (narrative timing), the *how much* (YTD-adjusted conviction sizing), and the *self* (comprehensive self-management infrastructure) to the execution framework from Art of Currency Trading. Full digest: `donnelly-alpha-trader-digest.md`. Checklists: `donnelly-alpha-trader-checklists.md`. |
| Donnelly — *The Art of Currency Trading* (2019) | 2026-04-20 | FX execution and trade management layer: practitioner-level fusion approach (fundamentals + technicals + behavioral + correlation + risk management → Five-Star trade). Core content: FX driver framework (4 global + 3 domestic drivers), delta vs. level principle, Dollar Smile model, interest rate/inflation regime matrix, Seven Deadly Setups (Slingshot Reversal, Hammers, Deviation from 100hr MA, Volume Spike, Broken Triangles, Double/Triple Top, Sunday Gaps) with quantitative entry/stop/target parameters, currency driver map (13 DM pairs × 2–4 drivers each), lead/lag correlation trading method, nine cognitive biases with FX-specific countermeasures, positioning vs. sentiment framework, NewsPivot concept and three data trading strategies, CB meeting EV grid, conviction-based position sizing (3-star 1% / 4-star 3% / 5-star 6%), monthly chunking (10% stop / 2× target), Kelly criterion (half/quarter-Kelly), stop loss methodology, slump protocol, overtrading prevention, 25 Rules of FX Trading. Method transfer: Donnelly provides the *how* of FX execution — entry timing, stop placement, position sizing, conviction grading, and trade management psychology. Extends the architecture from EM-only to include DM FX legs (essential because DXY views inform EM positions via the 65% global factor). Adds the first systematic behavioral self-management framework. Full digest: `donnelly-art-fx-trading-digest.md`. Checklists: `donnelly-art-fx-trading-checklists.md`. |

---

## 6. Standing Questions for the User

These are recurring questions the skill should revisit periodically as the user's thinking evolves:

- What is your typical risk budget and position sizing framework?
- What is your benchmark (if any) and tracking error tolerance?
- What is your typical holding period for macro trades?
- Which EM regions do you focus on most?
- What data sources and tools do you use for monitoring positions?

Understanding these allows more precise adversarial challenge — the right critique of a 1-week tactical trade is different from a 6-month structural position.
