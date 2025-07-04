# Divine-Ascension-System

This project simulates interactions between ontological agents that progress
through the states **Ego**, **Jaz**, and **Enotnost**. Each agent tracks its
internal **tension** and **emotion**. When tension exceeds `0.7` or emotion
exceeds `0.5`, the agent transitions to the next state:

1. **Ego** – believes truth is absolute and independent of others.
2. **Jaz** – believes truth is relative and shaped by relationships.
3. **Enotnost** – believes all truths are unified and interconnected.

Agents respond to questions based on their current state. The provided
`philosophical_dialogue` function demonstrates how two agents interact and
transition as their emotions increase.

## Running the example

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

## Running tests

Execute the unit tests with `pytest`:

```bash
python -m pytest -q
```

## Prerequisites

- Python 3.8 or newer
- No additional dependencies are required
