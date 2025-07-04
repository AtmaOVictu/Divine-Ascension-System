# Divine-Ascension-System

This project implements a small agent based framework where agents
transition between the philosophical states **Ego**, **Jaz** and
**Enotnost**.  Agents react to emotional intensity and tension which can
cause them to change state and influence their responses in dialogues.

## Usage

The package is self contained and requires only Python 3.11+.  To try
out a short dialogue run the following inside the repository:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
PY
```

## Running tests

Tests can be executed directly with `pytest`:

```bash
pytest -q
```

All tests should pass without the need to modify the Python path.

