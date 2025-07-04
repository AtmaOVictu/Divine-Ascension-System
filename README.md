# Divine-Ascension-System

A simple framework for experimenting with philosophical agents and state transitions.

## Installation

Create a virtual environment and install the testing dependency:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

## Running the tests

From the repository root run:

```bash
PYTHONPATH=. pytest -q
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# create two agents
alice = Agent("Alice")            # starts in Ego
bob = Agent("Bob", state="Jaz")   # starts in Jaz

# run a short dialogue
for line in philosophical_dialogue(alice, bob):
    print(line)
```

State transitions occur when an agent's emotion rises above `0.5` or their
accumulated tension exceeds `0.7`. Transitions follow the chain `Ego -> Jaz -> Enotnost`.
