# Divine-Ascension-System

This project provides a minimal framework for simulating philosophical
agents that transition between three ontological states:

* **Ego** – truth is absolute and individual.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents carry `tension` and `emotion` values which influence their state
transitions and responses. Dialogues demonstrate how agents with
different world views debate and evolve.

## Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install `pytest` for running tests:

   ```bash
   pip install pytest
   ```

## Running the Dialogue

Example usage demonstrating two agents debating truth:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2, exchanges=2):
    print(line)
```

## Running Tests

Execute the unit tests with:

```bash
pytest -q
```

All tests should pass, confirming correct state transitions and dialogue
behavior.
