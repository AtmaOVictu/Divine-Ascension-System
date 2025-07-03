# Divine-Ascension-System

This project contains a simple agent-based framework for exploring
philosophical dialogues. Agents move between the ontological states **Ego**,
**Jaz** and **Enotnost** according to their emotional intensity and tension.

## Installation

The core library has no external runtime dependencies beyond Python 3.  To run
the unit tests you will need `pytest`:

```bash
pip install pytest
```

## Running tests

The package has not yet been published to PyPI (see *Issue 2*).  Until the
packaging is updated you must include the repository on your `PYTHONPATH` when
running tests:

```bash
PYTHONPATH=. pytest -q
```

## Usage

Create two agents and start a philosophical discussion:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("Agent 1")
a2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

This prints a short conversation where the agents change state based on their
emotional levels and respond according to their current philosophy.
