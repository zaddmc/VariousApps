# Canasta in Python — Requirements & Roadmap

## 0. Scope & Assumptions

- **Variant**: Modern American Canasta, 4 players in 2 fixed partnerships (2v2). Rules below reflect this; 2-player and "Hand & Foot"-style variants are noted as future config options, not built in from the start.
- **Deck**: 2 standard 52-card decks + 4 jokers = 108 cards, shared stock.
- Three development phases, in order:
  1. Human vs human (local, same machine)
  2. Computer opponent: random → heuristic → learning agent
  3. Real-life "co-pilot" mode: track a physical game and evaluate decisions

The core design principle tying all three together: **the rules engine has no idea who or what is making decisions.** Humans, bots, and the assistant mode all talk to the same engine through the same interface. Get this separation right in Phase 1 and Phases 2–3 become additive, not rewrites.

---

## 1. Game Rules Reference (what the engine must enforce)

### 1.1 Cards & values

| Card    | Points | Notes                                                         |
| ------- | ------ | ------------------------------------------------------------- |
| Joker   | 50     | Wild                                                          |
| Ace     | 20     | Natural                                                       |
| 2       | 20     | Wild                                                          |
| 8–King  | 10     | Natural                                                       |
| 4–7     | 5      | Natural                                                       |
| Black 3 | 0      | Can only be melded when going out; blocks discard pile pickup |
| Red 3   | 100    | Bonus card, must be melded, not a playing card                |

### 1.2 Deal & setup

- 11 cards per player (4-player game), rest is the stock (drawing) pile.
- Discard pile starts empty.
- Team score carries across hands; game ends at 5000 points.

### 1.3 Turn structure

1. **Draw**: either 2 from top of stock, or 1 of the top of the discard pile and 1 from the stock, or the entire discard pile (if legal — see below).
2. **Meld** (optional, but required to pick up discard pile in some cases): lay down new melds or add to existing team melds.
3. **Discard**: exactly one card, face up, ending the turn.

### 1.4 Meld rules

- Meld = 3+ cards of same rank (jokers/2s wild).
- Max wild cards per meld: natural cards must always outnumber wild cards.
- A **Canasta** = 7+ cards in one meld.
  - **Natural canasta** (no wilds): 500 bonus.
  - **Mixed canasta** (contains wilds): 300 bonus.
- Minimum initial meld value required per team, based on **cumulative score**:

| Cumulative score | Min. initial meld |
| ---------------- | ----------------- |
| Negative         | 15                |
| 0–1495           | 50                |
| 1500–2995        | 90                |
| 3000+            | 120               |

### 1.5 Discard pile pickup

- Normally requires a matching natural pair in hand (to meld with the top card).
- Picking up the pile gives you all cards in it, not just the top one — must immediately be at least partially melded.

### 1.6 Red threes

- Drawn red 3s are placed face up immediately and 2 replacement cards are drawn.

### 1.7 Going out

- A team may go out only if they have completed at least the minimal required as described below.

  | Cumulative score | Req. Canasta |
  | ---------------- | ------------ |
  | Negative         | 1            |
  | 0–1495           | 1            |
  | 1500–2995        | 2            |
  | 3000+            | 3            |

- To go out the player must discard the last card which they have no other use for.
- Going out bonus: 100 points.

### 1.8 Scoring a hand

Per team: sum of melded card points + canasta bonuses + red 3 bonuses + going-out bonus − points still in hand of any player.

---

## 2. Architecture

Keep the **rules engine** and **players/agents** in separate packages from turn one.

```text
canasta/
  engine/
    card.py          # Card, Deck (2x52+jokers), comparisons
    meld.py          # Meld validation, canasta detection, wild-count rules
    hand.py          # Player hand container
    rules.py         # Legal-move generation, initial meld thresholds, freeze logic
    state.py         # GameState: stock, discard pile, teams, scores, turn, frozen flag
    engine.py        # Orchestrates turns, applies actions, emits events
  agents/
    base.py          # Agent interface: choose_draw(), choose_meld(), choose_discard()
    human_cli.py      # Wraps stdin/stdout for a human player
    random_agent.py
    heuristic_agent.py
    learning_agent.py
  assistant/
    tracker.py        # Ingests real-world game state from manual input
    advisor.py         # Suggests moves given partial/imperfect information
  cli/
    play_local.py      # Phase 1 entrypoint
    play_vs_bot.py      # Phase 2 entrypoint
    assist.py           # Phase 3 entrypoint
  tests/
```

Key data structures:

- `GameState` is the single source of truth — immutable-ish, or at least changes only through `engine.apply(action)`.
- Every action (draw, meld, discard) is logged as an event object. This event log is what Phase 2's learning agent will train on/against, and what Phase 3's advisor will use for post-game review — build it in Phase 1 even though you won't need it yet.
- `Agent` interface (abstract base class) exposes exactly the decisions a turn requires: draw source, which melds to make/extend, what to discard. Human, random, heuristic, and RL agents all implement this same interface, so the engine and CLI never need to know which kind of agent they're talking to.

---

## 3. Phase 1 — Human vs Human

**Goal**: a fully rules-correct 2-team, 4-player game, playable start to finish on one machine (players take turns at the keyboard, or hotseat).

Requirements:

- [ ] Full rules engine per Section 1, with exhaustive validation (illegal moves must be rejected with a clear reason, not silently allowed).
- [ ] Text/CLI interface: show your own hand, discard pile top + frozen state, team melds, opponent meld counts (not opponent hands).
- [ ] Save/load game state to JSON (useful for debugging and later for resuming assistant-mode sessions).
- [ ] End-of-hand scoring breakdown printed clearly (so you can sanity-check the engine against manual scoring by hand at first).
- [ ] Multi-hand game loop that continues until a team hits 5000.

This phase is where correctness matters most — bugs here propagate into every later phase. Budget real time for unit tests (Section 8).

---

## 4. Phase 2 — Computer Opponent

Build this as three progressively smarter agents behind the _same_ `Agent` interface, so you can always drop in an older version to benchmark against.

### 4a. Random agent

- Chooses uniformly among all legal actions the rules engine offers.
- Purpose: baseline, and a stress-test of your legal-move generator (if random play never crashes or produces illegal states, your engine is solid).

### 4b. Heuristic agent

Rule-of-thumb improvements, each independently toggleable so you can measure their individual effect:

- Prefer completing/extending a canasta over starting a new meld.
- Hold red 3s and discard them only when forced.
- Avoid discarding cards that would give the opponent an easy pickup (track what ranks they've shown interest in via their pickups).
- Respect freeze/minimum-meld constraints proactively rather than just legally.

### 4c. Learning agent

This is the ambitious part — worth scoping carefully:

- **State representation**: your hand, known melds (yours + opponents'), discard pile top + frozen flag, stock size, cumulative scores. Opponent hands are hidden — represent as unknown/zero.
- **Action space problem**: Canasta's true action space (which subset of cards to meld, which to discard) is huge and combinatorial. Don't model it as one flat action space. Decompose into sequential sub-decisions (draw source → meld-or-not → which meld → discard), each a smaller discrete choice, and let the agent make several small decisions per turn.
- **Suggested approach**: start with self-play between heuristic and random agents to generate a large dataset of (state, action, outcome) tuples, then either:
  - Train a value/policy network via self-play RL (e.g., PPO, using a lightweight framework rather than building the training loop from scratch), or
  - Start simpler: use a genetic algorithm / hill-climbing to tune the heuristic agent's weights against itself over many simulated games — much cheaper to implement and debug, and a reasonable stepping stone before deep RL.
- **Reward signal**: net score differential at end of hand/game; penalize illegal-move attempts during training if your action masking isn't airtight.
- **Evaluation**: maintain an Elo-like rating by round-robin between agent versions so "slowly getting better" is measurable, not just assumed.

---

## 5. Phase 3 — Real-Life Co-Pilot Mode

**Goal**: sit next to a real physical game, feed it what you can see, and get move suggestions / post-game evaluation. This is fundamentally an **imperfect-information advisor**, different in kind from Phases 1–2 where the engine sees everything.

Requirements:

- [ ] **Input**: manual entry interface for real-world state — your hand, current discard pile (full history, since pickups matter), team melds on the table, whose turn it is. Design the input format to be fast to type mid-game (short codes like `7H`, `0J` for joker, `2S` for wild). Camera/vision card recognition is explicitly out of scope for now — note it as a possible future extension.
- [ ] **Belief tracking**: since opponent hands are unknown, track the set of cards not yet seen (not in your hand, not in any discard/meld) as the pool your engine reasons over.
- [ ] **Decision support**: given the known state, suggest a draw/discard/meld decision. Approach: _determinization_ — sample many plausible opponent hands consistent with what's been seen, run your Phase 2 agent's evaluation on each sample, and aggregate (e.g., majority vote or expected value) into a recommendation. This reuses your learning/heuristic agent rather than requiring a separate imperfect-information model.
- [ ] **Live correction**: let you fix mis-entered state without restarting (physical games don't pause for typos).
- [ ] **Post-game report**: replay the event log, compare your actual choices to what the advisor would have suggested at each point, and summarize where the biggest gaps were.

---

## 6. Suggested Tech Stack

- Python 3.11+, `dataclasses` (or `pydantic` if you want validation for free on the assistant-mode input parsing).
- `pytest` for the rules engine — treat this as non-negotiable given how many edge cases Section 1 has.
- CLI: plain `input()`/`print()` is fine for Phase 1; consider `rich` or `textual` once you want the assistant-mode display to show more state at a glance.
- Phase 2c: PyTorch if you go the RL route; no extra dependency if you go the genetic-algorithm route on the heuristic weights.
- Persistence: JSON for game state and event logs (human-readable, easy to diff while debugging).

---

## 7. Testing Strategy

Prioritize rules-engine tests over everything else — this is the part where a subtle bug (e.g., miscounting wilds in a meld, or getting the freeze logic wrong) silently produces wrong outcomes for phases/hours before you notice. Cover explicitly:

- Meld validity boundary cases (exactly at the wild/natural ratio limit).
- Canasta bonus type (natural vs mixed) attribution.
- Discard pile freeze triggers and unfreeze conditions.
- Initial meld minimums at each cumulative-score threshold.
- Red three scoring in both the "melded" and "team never melded" cases.
- Going-out eligibility (must have a canasta).

## 8. Suggested Milestones

1. Engine + rules tests passing, no UI.
2. Phase 1 CLI playable end-to-end for a full game to 5000.
3. Random agent plugged in via `Agent` interface — confirms interface is truly implementation-agnostic.
4. Heuristic agent + Elo harness.
5. Learning agent v1 (genetic-tuned heuristic or first RL pass) beating heuristic agent consistently.
6. Assistant-mode input/tracking, no suggestions yet — just faithful state tracking of a real game.
7. Assistant-mode advisor using determinization + Phase 2 agent.

---

## Open Decisions for You

- Exact ruleset details vary by region/house rules (going-out permission, "Hand & Foot" style, whether black 3s can start a discard freeze differently). Worth locking down your specific house rules before writing rules-engine tests, since they encode the spec.
- 2-player vs 4-player as a config option, or 4-player only for now?
