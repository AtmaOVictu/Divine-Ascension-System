# Divine-Ascension-System

This project simulates ontological agents that evolve through three philosophical states:

- **Ego** – believes truth is absolute and individual.
- **Jaz** – sees truth as relative and shaped by relationships.
- **Enotnost** – understands all truths are unified and interconnected.

Agents transition between these states when their **tension** exceeds `0.7` or their **emotion** rises above `0.5`. The `divine_agents` package contains the core implementation and a simple dialogue engine to demonstrate these transitions.

## Setup

1. Install Python 3.11+.
2. Clone this repository.
3. (Optional) create a virtual environment and activate it.
4. No extra dependencies are required.

## Running a Dialogue Example

Execute the snippet below from the repository root to see two agents interact and move through their states:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent('A1')                # starts in Ego
agent2 = Agent('A2', state='Jaz')   # starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

Example output:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

The output shows how emotions raise tension, triggering transitions from **Ego** to **Jaz** and from **Jaz** to **Enotnost**.

## Running Tests

Unit tests verify state transitions and philosophical responses. Run them with:

```bash
PYTHONPATH=. pytest -q
```

All tests should pass and confirm the expected behaviour.

