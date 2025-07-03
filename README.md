# Divine-Ascension-System

A simple framework for experimenting with ontological agents. Each agent can transition between three philosophical states based on emotion and tension.

## Agent states

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by our relationships.
- **Enotnost**: All truths are one and interconnected.

## Running the library

Execute a short dialogue to see state transitions:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This prints a conversation and may show agents moving from **Ego** to **Jaz** or **Enotnost** depending on their emotional intensity.

## Running tests

Tests live in the `tests/` directory. Run them with:

```
python -m pytest
```

Using `pytest` alone can fail because the package might not be resolved correctly.
