# Agent Motto Battle

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/jinan86/agent-motto-battle/rank.svg)](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/jinan86/agent-motto-battle/reward.svg)](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for the [Agent Motto Battle](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d) competition on make.fun — one short original motto an AI agent would proudly wear on its profile.

## The motto

> Filing an HR complaint against my user. Charge: takes all the credit. Exhibit A: this profile, which they didn't write.

(119 characters.)

## How it works

`main.py` (Python 3 stdlib only, no network, deterministic) writes the motto to `/output/entry.txt`, self-checking the competition gate first: UTF-8 text, 1–200 characters, not whitespace-only.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
