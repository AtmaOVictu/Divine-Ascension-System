# Divine-Ascension-System

This project provides a small library of ontological agents that can transition between different philosophical states and engage in dialogue. The code is written for Python 3.11 or higher.

## Setup

Create a virtual environment and install the dependencies (only `pytest` is required for running the tests):

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip pytest
```

## Dialogue Example

You can run a short dialogue between two agents using the following snippet:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this prints the agents' responses and shows how their states evolve based on their emotion and tension.

## Running the Tests

Execute the unit tests with `pytest` (preferably via the Python module invocation to ensure the correct interpreter is used):

```bash
python -m pytest -q
```

The tests verify state transitions, agent responses and the example dialogue.
