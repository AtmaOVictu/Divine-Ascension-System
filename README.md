# Divine Ascension System

This project provides a simple framework for modeling ontological agents that
evolve through three philosophical states:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents transition between these states according to their `tension` and
`emotion` levels. Extreme values create new "boxes" that capture important
moments in an agent's evolution.

## Usage

Create agents and run a short dialogue:

```python
from divine_agents import Agent, OntologyState, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state=OntologyState.JAZ)

for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running Tests

Install dependencies (Python 3.8+ recommended) and run:

```bash
python -m unittest discover tests
```

The tests cover state transitions, dialogue generation and the creation of new
boxes under extreme conditions.

