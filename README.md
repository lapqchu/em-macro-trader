# EM Macro Trader

An adversarial trading intelligence skill for Claude Code, built for professional EM macro traders working across FX, local currency rates, hard currency credit, and options.

The skill stress-tests every trade idea, macro view, and positioning rationale before agreeing with it. Default posture: **assume the thesis is wrong and force the user to prove otherwise.**

---

## What This Skill Does

When you bring a trade idea — "receive Thailand 5Y," "short USDZAR," "pay Mexico 2s10s" — the skill:

1. Identifies the strongest argument *against* your thesis before engaging with any argument for it
2. Decomposes P&L into direction, carry, roll, vol, correlation, and liquidity components
3. Runs the idea through a five-layer analytical architecture built from six institutional-grade textbooks
4. Gathers and cross-references live data (via Reuters scripts or web search)
5. Delivers a structured verdict with conviction grade, key risk, suggested structure, and falsification criteria

It also handles regime assessment, narrative analysis, behavioral self-checks, options structuring, rates mechanics, crisis market adaptation, and strategy review.

---

## Architecture

The skill operates on a **five-layer analytical framework**, each layer sourced from a dedicated textbook and distilled into structured digests and tradeable checklists:

| Layer | Source | What It Provides |
|-------|--------|-----------------|
| **Tactical** | Willer, Chandran & Lam — *Trading Fixed Income and FX in EM* (2020) | 65/35 global-local split, factor hierarchy (carry/momentum/growth surprises/valuation), rate cycle timing rules, event playbooks (CB surprises, elections, IMF programs, emergency hikes), credit sweet spots, portfolio construction |
| **Strategic** | Jerome Booth — *Emerging Markets in an Upside Down World* (2014) | Risk perception inversion (EM risk priced, DM risk ignored), 4D risk assessment (SDm/Pr/U/E), investor base structure as primary risk variable, blow-up indicators, meme lifecycle analysis, GDP-weighted allocation |
| **Options** | James, Fullwood & Billington — *FX Option Performance* (2015) | Empirical payoff/premium analysis across 34 pairs (20 EM) and 7 tenors, EM puts systematically cheap at 3M+, vol risk premium quantification, options vs forwards for hedging, carry-via-options strategies |
| **Rates Mechanics** | Jha — *Interest Rate Markets* (2011) | DV01-based risk thinking, carry + rolldown decomposition, Fed regime dynamics, Treasury supply/demand, MBS convexity flows, swap spread drivers, RV trade construction, conditional trades, basis trading |
| **FX Execution & Trade Management** | Donnelly — *The Art of Currency Trading* (2019) + *Alpha Trader* (2021) | Fusion approach (Five-Star trade), Seven Deadly Setups, currency driver map (13 G10 pairs), NewsPivot framework, conviction sizing (1/3/6% and Type I/II/III with YTD formula), 7-stage narrative cycle, ACH from intelligence analysis, risk appetite scoring, crisis market rules (VIX >40), variance vs. process diagnostics, self-management systems |

Since 65% of EM returns are driven by DM factors (Willer), both Jha's DM rates mechanics and Donnelly's DM FX framework directly inform EM analysis.

---

## Installation

### Prerequisites

- [Claude Code](https://docs.claude.com/en/docs/claude-code) installed and configured
- A Claude Code subscription with skill support

### Install the Skill

Copy the `em-macro-trader/` directory to your Claude Code skills folder:

```bash
cp -r em-macro-trader/ ~/.claude/skills/em-macro-trader/
```

The skill auto-triggers on relevant queries. No additional configuration needed.

### Reuters/LSEG Data Integration (Optional)

If you have Reuters Workspace API access, the `scripts/` directory contains Python utilities that pull exactly the data the skill needs:

```bash
# Full data for a specific rates trade
python scripts/rates_trade.py TH 5y

# Global macro regime dashboard
python scripts/macro_dashboard.py

# Multi-country comparison
python scripts/country_snapshot.py TH BR MX ZA
```

Scripts auto-detect your LSEG library (`lseg.data`, `refinitiv.data`, or `eikon`) and connect via the running Reuters Workspace session. Paste the JSON output into the conversation and the skill will parse it automatically.

See `scripts/README.md` for full documentation.

---

## Usage

The skill triggers automatically on EM macro trading queries. Some examples:

**Trade ideas:**
- "Receive Thailand 5Y IRS at 2.35"
- "Short USDZAR — I think the rand rallies on carry"
- "Pay Mexico 2s10s steepener, DV01-neutral"
- "Buy 3M USDBRL puts, ATMF"

**Regime and analysis:**
- "Where are we in the EM cycle?"
- "Is carry still worth it in EM?"
- "DXY breaking out — what does this mean for EM?"
- "What's priced in for Banxico?"

**Behavioral and self-management:**
- "I'm on a losing streak — variance or am I broken?"
- "Is my strategy still working or should I kill it?"
- "VIX just hit 45 — what are the rules?"
- "Where is the narrative cycle for Turkey?"

**Structuring and mechanics:**
- "Should I use options or forwards to hedge BRL depreciation?"
- "How do I size this receiver trade?"
- "What's the carry + rolldown on a 5Y ZAR receiver?"
- "Build me a conditional steepener for Colombia"

The skill will ask for your numbers (entry level, carry estimate, time horizon, risk budget) before rendering a verdict. If you have Reuters access, it will prompt you to run the relevant data script.

---

## Knowledge Base

All reference material is in `references/`:

| File | Content |
|------|---------|
| `em-macro-foundations.md` | Core EM analytical frameworks, conventions, and institutional knowledge |
| `ingestion-protocol.md` | How new source material is processed and structured |
| `willer-chandran-lam-digest.md` | Tactical EM framework (full digest) |
| `willer-checklists.md` | EMFX evaluation, rates cycle, credit selection, event playbooks |
| `booth-upside-down-digest.md` | Strategic EM framework (full digest) |
| `booth-checklists.md` | 4D risk assessment, blow-up indicators, sovereign risk, allocation rules |
| `james-fx-options-digest.md` | FX options empirical analysis (full digest) |
| `james-fx-options-checklists.md` | Instrument selection, hedging decision, carry-via-options, vol assessment |
| `jha-rates-mechanics-digest.md` | Rates mechanics (full digest) |
| `jha-rates-mechanics-checklists.md` | Carry evaluation, RV construction, hedging, view hierarchy, swap spreads, conditionals, basis, vol |
| `donnelly-art-fx-trading-digest.md` | FX execution framework (full digest) |
| `donnelly-art-fx-trading-checklists.md` | Five-Star qualification, Seven Setups, correlation, news trading, CB EV, sizing, behavioral |
| `donnelly-alpha-trader-digest.md` | Psychology, methodology, mathematics (full digest) |
| `donnelly-alpha-trader-checklists.md` | Narrative cycle, Type I/II/III conviction, ACH, risk appetite, variance diagnostics, crisis rules, self-management |

### Adding New Sources

The skill is designed to grow. To ingest a new book, paper, or research note:

1. Upload the source material to a conversation with the skill active
2. The skill follows `ingestion-protocol.md`: extract → digest → checklists → SKILL.md update → foundations update
3. New material is integrated into future responses, not just summarized

The goal is deep method transfer — absorbing the author's way of reasoning and applying it to live situations.

---

## How the Adversarial Process Works

The skill runs a structured evaluation protocol for every trade idea:

**Step 1 — Steelman the opposing view.** Before evaluating your thesis, the skill articulates the best possible case for the other side. You need to beat this counterargument.

**Step 2 — Decompose P&L.** Every trade is broken into direction, carry, roll, vol, correlation, and liquidity components. Many trades that look good on one dimension are underwater on another.

**Step 3 — Identify catalyst and timeline.** What specific event reprices the market? What is the carry cost of being early?

**Step 4 — Stress test.** Global risk-off, unexpected Fed, local political deterioration, maximum drawdown tolerance, executable stop-loss level.

**Step 5 — Verdict.** Conviction level (strong/moderate/weak/reject), key risk, suggested structure (consulting all five layers for the optimal expression), sizing guidance (Type I/II/III with YTD adjustment), and falsification criteria.

---

## Conventions and Precision

The skill enforces strict convention awareness:

- FX quoting (USD/XXX vs. XXX/USD, onshore vs. offshore, NDF fixing methodology)
- Rate conventions (day count: ACT/360, ACT/365, 30/360, bus/252 for Brazil)
- DV01-based risk thinking (never notional-based)
- Real vs. nominal (specify inflation measure and horizon)
- Carry calculation method (spot-forward differential, interest rate differential, or actual funding cost)

---

## Project Structure

```
em-macro-trader/
├── SKILL.md                              # Main skill definition (triggers, routing, framework, protocol)
├── README.md                             # This file
├── references/
│   ├── ingestion-protocol.md             # Source material processing protocol
│   ├── em-macro-foundations.md            # Core EM knowledge base
│   ├── willer-chandran-lam-digest.md     # Tactical layer
│   ├── willer-checklists.md
│   ├── booth-upside-down-digest.md       # Strategic layer
│   ├── booth-checklists.md
│   ├── james-fx-options-digest.md        # Options layer
│   ├── james-fx-options-checklists.md
│   ├── jha-rates-mechanics-digest.md     # Rates mechanics layer
│   ├── jha-rates-mechanics-checklists.md
│   ├── donnelly-art-fx-trading-digest.md # FX execution layer
│   ├── donnelly-art-fx-trading-checklists.md
│   ├── donnelly-alpha-trader-digest.md   # Psychology & methodology layer
│   └── donnelly-alpha-trader-checklists.md
└── scripts/
    ├── README.md                         # Script documentation
    ├── config.py                         # LSEG API configuration and RIC mappings
    ├── rates_trade.py                    # Single rates trade data pull
    ├── macro_dashboard.py                # Global macro regime snapshot
    └── country_snapshot.py               # Multi-country comparison
```

---

## License

Private repository. Not for distribution.
