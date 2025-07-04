# Divine-Ascension-System

This repository contains a small agent-based framework used to simulate philosophical
conversations. Agents move between the ontological states **Ego**, **Jaz**, and
**Enotnost** based on their emotional intensity and tension levels.

## Overview

Agents are defined in `divine_agents/agent.py` and can transition between the
three states when their `tension` exceeds `0.7` or their `emotion` exceeds
`0.5`. Each state influences how an agent perceives truth:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by our relationships.
- **Enotnost** – all truths are unified and interconnected.

A simple dialogue simulation is provided in `divine_agents/dialogue.py`.
It creates two agents, adjusts their emotional levels, and prints a few lines of
debate demonstrating state transitions.

## Setup

The project requires **Python 3.8+** and has no external dependencies beyond
the standard library. Clone the repository and ensure Python is available in
your environment.

```bash
python --version  # should show Python 3.8 or newer
```

## Running the Dialogue Simulation

Open a Python interpreter or create a small script that imports the `Agent`
class and the `philosophical_dialogue` function:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Executing this code will display a short conversation between the two agents as
they shift states and respond according to their philosophical stance.

## Running Tests

Unit tests reside in the `tests` directory and use the standard `unittest`
module. To run the complete test suite, execute:

```bash
python -m unittest discover tests
```

or with `pytest` if installed:

```bash
pytest -q
```

The tests verify state transitions, response generation, and that the dialogue
simulation produces expected output.

