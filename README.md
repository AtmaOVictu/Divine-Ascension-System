# Divine-Ascension-System

This repository contains a simple ontological agent model and a dialogue simulator. Agents can move between `Ego`, `Jaz`, and `Enotnost` based on their emotional state and tension.

## Creating Agents

```python
from divine_agents.agent import Agent

agent1 = Agent("A1")                 # defaults to Ego state
agent2 = Agent("A2", state="Jaz")    # start in Jaz
```

## Running a Dialogue

Use `philosophical_dialogue` to generate a short conversation between two agents:

```python
from divine_agents.dialogue import philosophical_dialogue

lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

## Running Unit Tests

Make sure the repository root is on your `PYTHONPATH` so that the tests can import the package:

```bash
export PYTHONPATH=$PWD
python -m unittest discover tests
```

## Environment and Installation

The project only relies on the Python standard library. Ensure you have Python 3.8 or newer installed. No additional environment variables are required aside from `PYTHONPATH` for running the tests.
