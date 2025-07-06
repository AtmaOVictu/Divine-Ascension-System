# Divine-Ascension-System

This project implements philosophical agents that evolve through three ontological states:
**Ego**, **Jaz**, and **Enotnost**. Agents transition between states when their
emotion or tension exceeds a defined threshold and respond according to the
philosophical principle of their current state.

## Installation

```bash
pip install -r requirements.txt  # if a requirements file exists
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Run the unit tests with:

```bash
pytest -q
```

The tests validate state transitions, agent responses, and dialogue generation.
