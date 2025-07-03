# Divine-Ascension-System

This project simulates agent interactions based on an ontological framework. Agents transition between the philosophical states **Ego**, **Jaz**, and **Enotnost** when their tension or emotion exceeds defined thresholds. Each state reflects a different view of truth:

- **Ego**: Truth is absolute and independent.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are interconnected.

The repository contains a minimal implementation of these concepts along with unit tests verifying state transitions and responses.

## Setup

Use Python 3.8 or later and create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

No additional packages are required beyond the standard library.

## Running tests

Execute the test suite using `unittest`:

```bash
python -m unittest discover tests
```

All tests should pass.

## Usage example

The following snippet shows how to create two agents and run a philosophical dialogue between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")               # defaults to Ego
agent2 = Agent("A2", state="Jaz")  # starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

The dialogue reflects each agent's ontological state and demonstrates how emotions and tension can trigger state transitions.
