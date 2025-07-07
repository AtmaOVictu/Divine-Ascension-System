# Divine-Ascension-System

Divine-Ascension-System is a small experimental playground for exploring ontological agents that shift between three philosophical states: **Ego**, **Jaz**, and **Enotnost**. Agents transition when their emotion or tension levels exceed certain thresholds and then respond to questions about truth from the perspective of their current state. The system includes a simple dialogue simulation and unit tests demonstrating the behaviour.

## Installation

Packaging is not yet provided, but once a `pyproject` or `setup.py` is available you will be able to install the project in editable mode:

```bash
pip install -e .
```

Until then you can run it directly from the repository.

## Running tests

Use `pytest` with the repository on your `PYTHONPATH`:

```bash
PYTHONPATH=. pytest
```

## Usage example

The snippet below shows how to create two agents and start a short dialogue using `philosophical_dialogue`:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This will output lines where each agent states their view of truth, transitions to a new state based on updated emotion, and responds again in the new state.
