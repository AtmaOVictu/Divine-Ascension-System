# Divine-Ascension-System

Divine-Ascension-System is a minimal framework for modelling philosophical
agents.  Each agent inhabits one of three ontological states and may transition
between them according to its emotional intensity and tension.  The goal of the
project is to demonstrate how emotions and debate can lead agents from an
individual view of truth (**Ego**) toward a relative view (**Jaz**) and finally
to a unified understanding (**Enotnost**).

## Installation

The project has no external dependencies beyond Python 3.  Clone the repository
and install an optional test runner if desired:

```bash
python -m pip install pytest  # optional, for running tests with pytest
```

## Running the Tests

Unit tests live in the `tests/` directory.  They can be executed using the
standard library's `unittest` module or with `pytest`:

```bash
# With unittest
python -m unittest discover -s tests

# Or with pytest
pytest
```

## Quick Example

The snippet below shows how to create two agents and run a short dialogue
between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

This will display a simple conversation where each agent responds according to
its current state and may transition when their tension or emotions increase.
