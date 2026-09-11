# Divine Ascension System

This project models a small ontological framework where agents evolve
through three philosophical states: **Ego**, **Jaz**, and **Enotnost**.
Agents update their emotion and tension values during dialogue which
in turn drives their transitions between these states.

## Usage

Create agents and start a short dialogue:

```python
from divine_agents import Agent, OntologyState, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state=OntologyState.JAZ)
for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running Tests

Install the required version of Python (3.8+ recommended) and run:

```bash
python -m unittest
```

The tests verify state transitions, dialogue output and that extreme
values create new "boxes" representing additional phases for the agent.

