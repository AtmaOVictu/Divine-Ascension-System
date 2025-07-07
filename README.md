# Divine-Ascension-System

Small framework for experimenting with ontological agents.  The project
includes an ``Agent`` class for modelling philosophical states and a helper
function for generating short dialogues.

## Installation

Clone the repository and install any optional dependencies.  The project has no
strict requirements, so a standard Python 3 environment is sufficient.

```bash
git clone https://github.com/youruser/Divine-Ascension-System.git
cd Divine-Ascension-System
```

## Running tests

The repository contains a small unittest suite.  Run it with ``pytest``:

```bash
python -m pytest -q
```

## Modules

### ``divine_agents.agent``

Defines the ``Agent`` class representing an entity that can transition between
the philosophical states ``Ego``, ``Jaz`` and ``Enotnost``.  Each agent stores a
tension and emotion level which, when above the thresholds, trigger state
changes via ``Agent.transition``.  The ``Agent.respond`` method returns a
statement reflecting the agent's current state.

### ``divine_agents.dialogue``

Contains ``philosophical_dialogue`` which accepts two ``Agent`` instances and
simulates a short conversation.  During the interaction both agents update their
emotions, potentially leading to state transitions.

## Example usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

This will print a few lines of dialogue while demonstrating the state transition
logic of the agents.
