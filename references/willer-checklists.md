# Tradeable Checklists — Extracted from Willer, Chandran & Lam

These are decision tools extracted from "Trading Fixed Income and FX in Emerging Markets" for use during live trade evaluation.

---

## Checklist 1: EMFX Trade Idea Evaluation

Before putting on a directional EMFX trade, answer ALL of these:

### Global Regime (65% of the return)
- [ ] What is DXY doing? (dominant driver — nothing else matters if you're wrong on this)
- [ ] What are US HY spreads doing? (more reliable than VIX as EM leading indicator)
- [ ] What is the China credit impulse / monetary conditions doing? (200-day MA z-score)
- [ ] Is the Fed hiking, cutting, or on hold? Is this a "benign" or "aggressive" cycle?
- [ ] What is the max z-score across EMFX IV, G10 IV, US rates IV, S&P IV, oil IV? (>2 = cut exposure)

### Country Selection
- [ ] What is the vol-adjusted carry? (inverse prior-year realized vol × carry; JPY or EUR funded?)
- [ ] What are growth surprises doing? (Citi EM surprise index; crossing zero from below = bullish)
- [ ] What is 1-month momentum saying? (vol-adjusted; best short-term signal)
- [ ] Is breadth improving or deteriorating? (count up vs. down days across EM basket)
- [ ] Are there seasonal effects in play? (10yr lookback, >1% threshold, weekly rebalance)
- [ ] What is the PPP z-score (10yr lookback)? (modest value, but directionally helpful)
- [ ] Ignore: current account level (money-losing), interest rate differentials (inverse of G10)

### Trade Structure
- [ ] What is the carry cost of being wrong? (positive or negative; how long can you hold?)
- [ ] Is there a natural hedge? (HUF, SEK, EUR, CZK for beta >1 + negative carry)
- [ ] What is the correlation regime? (idiosyncratic or beta trade?)
- [ ] Can you express this as a relative value vs. a correlated pair at equal vol?

---

## Checklist 2: EM Rates Cycle Position

### Where Are We in the Cycle?
- [ ] Has the 1yr swap crossed below (above) the policy rate from above (below)?
- [ ] Has inflation peaked? (EM CBs stop hiking the same month inflation peaks)
- [ ] What is the real policy rate? (nominal minus current inflation — level matters)
- [ ] Is the CB constrained by FX? (cannot be bullish rates and bearish FX simultaneously)
- [ ] Is the CB constrained by commodities? (except commodity exporters where relationship inverts)
- [ ] Is the Fed constraining the local CB? (Fed hikes → USD strength → EMFX weakness → forced EM tightening)

### Signal Confirmation
- [ ] Is the term premium elevated? (>1 std dev on 3-month rolling → receive 5Y)
- [ ] Where are breakevens vs. inflation target? (<target midpoint = buy linkers)
- [ ] What is the real rate ranking vs. EM peers?
- [ ] Is the curve shape consistent with the cycle position? (steepeners before first cut; flatteners before first hike)

### Trade Expression
- [ ] Outright receiver/payer vs. steepener/flattener? (steepeners often have better Sharpe)
- [ ] Cash or swap? (swap enables DV01-neutral, tax advantages in Brazil/Colombia/Indonesia)
- [ ] Nominals or linkers? (linkers during hiking cycles / commodity rallies / EMFX weakness; nominals during easing / UST rallies)

---

## Checklist 3: EM Credit Country Selection

### Factor Assessment
- [ ] What is the vol-adjusted carry rank? (HY vs. IG carry still works in credit, unlike EMFX)
- [ ] What is 12-month vol-adjusted momentum? (IR 0.7; monthly rebalance)
- [ ] What is the spread vs. exponential rating curve? (residual = relative value signal)
- [ ] Is this a BB, 3-5yr bond? (sweet spot: IR 1.32)

### Structural Risk
- [ ] Does this country have a pegged currency + commodity exposure? (worst combination in downturns)
- [ ] Is an IMF program in play? (wait for first pullback post-announcement; 150-day tightening)
- [ ] Rating agency trajectory? (1st IG loss → position for 2nd; 2nd IG loss → buy on forced selling)
- [ ] Is the UST curve inverted or disinverting? (disinversion = cut credit risk)

### Trade Expression
- [ ] Front-end leveraged vs. back-end unleveraged? (Buffett trade: front-end leveraged wins)
- [ ] External vs. local? (overweight external when bullish US HY; FX-hedged basis)
- [ ] ISM timing? (when ISM peaks in high 50s → reduce HY, increase IG, shorten duration)

---

## Checklist 4: Event Playbook Quick Reference

### FX Intervention Expected?
- Brazil: >1.5% underperformance / 5 days → likely; need >USD 2.5B/day to matter
- Mexico: ~1% over 15 days → likely; first intervention most effective
- Trade: long local FX vs. EMFX index for ~10 trading days

### Emergency Rate Hike Announced
- Check: >30 daily std dev moves pre-hike AND REER negative? → likely to work (12/20 success)
- If REER positive → hike likely fails; don't chase
- Rates: avoid receiving day 1; start receiving around day 50-75; full unwind ~1 year
- FX: stabilizes after several days if preconditions met

### IMF Package Announced
- FX: continues weak 5-25 days; turns positive at ~25 days; full stabilization ~3 months
- Credit: widening continues initially; wait for pullback; median 100bp+ tightening over 150 days
- Rule: patience; don't rush in

### Election in 3 Months
- Default pattern: weakness until 2 weeks before → strong rally through 3 months post
- Even market-unfriendly winners follow this pattern (political incentives to delay pain)
- Trade: fade pessimism at T-2 weeks

### Inflation Surprise
- Follow-through: 1-1.5 additional std dev over 20-25 days
- Strongest in: Mexico, Hungary, Russia, India (positive); Chile, Hungary, Peru, Turkey (negative)
- Avoid: Taiwan (reverses), China/Poland (no follow-through)

### CB Meeting Surprise (2+ std dev move in 2Y)
- Dovish: 1.5 std dev follow-through over 25 days
- Hawkish: 1.0 std dev follow-through over 20 days
- Best dovish: Thailand, Israel, Colombia, Chile, Czech, Korea
- Best hawkish: Hungary, Indonesia, Czech, Thailand

### Index Inclusion
- Bonds: 50-100bp rally post-announcement; additional 10-50bp on inclusion
- FX: minimal impact
- Don't take profits until 50%+ included

### Domestic Disaster (>1% GDP damage)
- Receivers rally 20-50bp first 5 days; peak ~20 days; 80%+ revert
- Only 2/7 led to actual CB easing — mostly a fade
