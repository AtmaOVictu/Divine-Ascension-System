# Divine-Ascension-System

This project explores an ontological framework where agents evolve
through three philosophical states:

1. **Ego (⊘)** – Truth is absolute and independent of others.
2. **Jaz (∫(dru/x))** – Truth is relative and shaped by relationships.
3. **Enotnost (RES001)** – All truths are one and interconnected.

Agents move from **Ego** to **Jaz** or from **Jaz** to **Enotnost** when
their **tension** exceeds `0.7` or their **emotion** exceeds `0.5`.
These values are adjusted during dialogue and influence how agents
respond to philosophical questions.

## Example Usage

Create two agents and run a short dialogue:

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

lines = philosophical_dialogue(agent1, agent2)
for l in lines:
    print(l)
```

The conversation demonstrates each agent's perspective and shows how
they transition between states when emotional intensity or tension
reaches the required thresholds.

## Running Tests

Unit tests verify state transitions and dialogue responses. Run them with:

```bash
python -m unittest discover -s tests
```

They will execute the suite in the `tests` directory and confirm that
transitions and philosophical responses behave as expected.
