# Divine-Ascension-System

This project provides a minimal framework for modelling philosophical agents that
transition between three ontological states: **Ego**, **Jaz** and **Enotnost**.
Transitions depend on each agent's emotion and tension levels.

## Philosophical States

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are one and interconnected.

## Installation

The package can be installed in editable mode:

```bash
pip install -e .
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Execute the unit tests with `pytest`:

```bash
pytest -q
```


