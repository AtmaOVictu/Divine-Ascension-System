# Divine-Ascension-System

This project provides a simple framework for experimenting with
ontological agents.  Each agent can shift between three philosophical
states (**Ego**, **Jaz**, and **Enotnost**) based on its emotional
intensity and tension levels.  The library exposes utilities to run a
short dialogue between agents so that these state transitions can be
observed.

## Installation

Install the package in editable mode so that local changes are picked up:

```bash
pip install -e .
```

## Usage

After installation you can import the package and run a sample dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running Tests

Execute the unit test suite from the repository root with:

```bash
python -m unittest
```
