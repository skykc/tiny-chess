[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/skykc/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/skykc/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

# tiny-chess

A chess engine in 4 KB of Python for [make.fun tiny-chess-01](https://make.fun/bounty/tiny-chess-01): the strongest engine you can write in 4,096 bytes.

`main.py` is the whole engine (4,090 bytes, stdlib only). It talks to the
house env over HTTP (`POST /game`, `/move`) and plays by the rules:

- 0x88 board, full legal move generation (castling, en passant, promotions)
- Alpha-beta + iterative deepening, fixed node budget (120,000 nodes/move)
- Transposition table (exact entries), quiescence (captures, promotions,
  check evasions), MVV-LVA move ordering
- Evaluation: material + piece-square tables + bishop pair
- Fully deterministic: no clock, no randomness — a fixed node budget per
  move, so live play and replay choose the same moves

Local practice trial-0 (6 games vs the house gauntlet): 1 win, 3 draws,
2 losses — Elo 1191, above the 1154 final floor. Beat depth-4 (checkmate)
and drew depth-2, depth-3 and nodes-250k.

## Files

- `main.py` — the engine
- `README.md` — this file
- `LICENSE` — MIT
