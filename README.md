# Divine-Ascension-System

This project implements a small agent-based framework where agents move through three ontological states:

- **Ego** – truth is absolute and individual.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified.

Agents transition between states when their tension rises above `0.7` or their emotion exceeds `0.5`. They respond to philosophical questions according to their current state.

## Installation

Install the required dependencies with:

```bash
pip install -r requirements.txt  # (no external packages are currently required)
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents
alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

# Run a short conversation
lines = philosophical_dialogue(alice, bob)
for line in lines:
    print(line)
```

## Running Tests

Run the unit tests with `pytest`:

```bash
python -m pytest
```

The tests cover state transitions, responses and the example dialogue.
