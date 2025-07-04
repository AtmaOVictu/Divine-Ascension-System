# Divine-Ascension-System

This project demonstrates an ontological agent system where agents transition between three philosophical states—**Ego**, **Jaz**, and **Enotnost**—based on their emotional intensity and tension. Agents debate the nature of truth from these perspectives, showing how emotion influences dialogue.

## Running the dialogue example

Use Python to run a small conversation between two agents:

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

## Running the tests

Unit tests verify state transitions and philosophical responses. Execute them with:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

## Requirements

* Python 3.8 or newer
* No external dependencies (only the Python standard library is used)
