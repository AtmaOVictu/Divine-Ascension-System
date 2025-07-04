# Divine-Ascension-System

This project simulates philosophical conversations between ontological agents.

## Ontological states
Agents may be in one of three states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by our relationships.
- **Enotnost** – all truths are one and interconnected.

An agent transitions from **Ego** to **Jaz** or from **Jaz** to **Enotnost** when
its `tension` rises above `0.7` or its `emotion` exceeds `0.5`.

## Installation
The code has no external dependencies aside from Python 3. Install Python and
clone this repository. No additional packages are required.

## Running the philosophical dialogue
To see a short dialogue between two agents run:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Agent 1 starts in Ego; Agent 2 starts in Jaz
agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

## Running tests
The unit tests can be executed with the built-in `unittest` runner:

```bash
python -m unittest discover -s tests
```
