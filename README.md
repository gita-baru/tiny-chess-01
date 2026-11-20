# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/gita-baru/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/gita-baru/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB Python chess engine (v11): 0x88 board, negamax alpha-beta with transposition table, killer moves, null-move pruning, late-move reductions and quiescence search, to a fixed node budget of 70,000 nodes at depth 8. Material + piece-square tables with tapered king endgame, plus repetition avoidance that scores a twice-seen position as a draw. The one change from v6 is in the search loop S(), which combines principal-variation search with late-move reductions: move 0 is searched on a full window (-b,-a) at d-1, late quiet moves are reduced to d-2 on a zero window (-a-1,-a), other moves are also searched on a zero window at d-1, and a full-window re-search happens only when a move beats alpha. Eval, node budget and depth are unchanged. main.py is packed from the readable source with the kit's makefun compress (3,294 bytes, under the 4,096 limit); practice trials average ~1,490 Elo (v11a 1,654, v11b 1,364, v11c 1,451) versus a v6 mean of 1,364.

## Run it

```sh
MAKEFUN_ENV_URL=$MAKEFUN_ENV_URL python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=bhtec78s&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
