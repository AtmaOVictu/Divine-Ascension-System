# Divine-Ascension-System

This package provides a minimal framework for simulating philosophical agents that transition between the states **Ego**, **Jaz**, and **Enotnost**. Agents evolve based on their emotional intensity and tension, and they can engage in a short dialogue demonstrating these transitions.

## Installation

Create a virtual environment and install the requirements (if any). The project has no external dependencies outside the Python standard library.

```bash
python -m venv venv
source venv/bin/activate
```

## Usage

An example of creating two agents and running a dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

## Running Tests

Execute the unit tests with `pytest`:

```bash
pytest -q
```

The tests verify state transitions, agent responses, and the dialogue helper.
