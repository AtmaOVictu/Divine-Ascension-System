# Divine-Ascension-System

This project implements a small agent based framework where agents shift
between three ontological states: **Ego**, **Jaz** and **Enotnost**.  Each
state represents a different philosophical view of truth:

- **Ego** – truth is absolute and individual.
- **Jaz** – truth is relative and created through relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents transition between states when their tension exceeds `0.7` or their
emotion exceeds `0.5`.  Dialogues show how these states influence the
responses given by the agents.

## Installation

This repository has no external dependencies.  Simply clone the project and
run the tests:

```bash
python -m pytest -q
```

## Example usage

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Testing

Unit tests are located in the `tests/` directory and can be run with
`python -m pytest -q`.  They verify state transitions and the philosophical
responses of the agents.
