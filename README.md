# Divine-Ascension-System

This project implements a simple agent-based framework that explores
philosophical concepts through dialogue. Agents transition between
three ontological states:

* **Ego** – truth is absolute and independent.
* **Jaz** – truth is relative and shaped through relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents hold an emotion level and type which can trigger state changes
when tension or emotion exceed configured thresholds.

## Installation

The project has no external dependencies. Clone the repository and run
the unit tests with Python 3.11 or later.

```bash
pip install -r requirements.txt  # if requirements are added
```

## Running Tests

From the repository root simply run:

```bash
pytest -q
```

All tests should execute without additional environment configuration.

## Usage

You can experiment with the agents in an interactive shell:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```

This will simulate a short philosophical debate where each agent may
shift state based on its emotional intensity.
