# Divine-Ascension-System

An agent-based framework where characters move through the ontological states
of **Ego**, **Jaz** and **Enotnost**. Each agent maintains a level of `tension`
and `emotion`. When `tension` surpasses `0.7` or `emotion` rises above `0.5`,
the agent transitions to the next state:

1. `Ego` → `Jaz`
2. `Jaz` → `Enotnost`

These thresholds are configurable through constants in
`divine_agents/__init__.py`.

## States overview

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative, shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

## Running the example dialogue

The file `divine_agents/dialogue.py` contains `philosophical_dialogue`, which
demonstrates a short conversation and state transitions:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")              # starts in Ego
a2 = Agent("A2", state="Jaz") # starts in Jaz

for line in philosophical_dialogue(a1, a2):
    print(line)
PY
```

## Running unit tests

All tests are in the `tests` directory and can be executed with:

```bash
python -m unittest discover -s tests -v
```

## Configuration options

The module `divine_agents/__init__.py` exposes two constants controlling state
changes:

```python
TRANSITION_TENSION_THRESHOLD = 0.7
TRANSITION_EMOTION_THRESHOLD = 0.5
```

Adjust these values to fine-tune how quickly agents move between states.
