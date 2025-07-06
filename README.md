# Divine-Ascension-System

This project implements a simple agent based model for exploring ontological states.
Agents may exist in three states:

* **Ego** – truth is considered absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents transition between states when tension exceeds `0.7` or emotion exceeds
`0.5`. Dialogue between agents reflects their current state and emotional level.

## Installation

The project has no external dependencies. Clone the repository and ensure that
Python 3.11 or newer is available.

```bash
python -m pip install -r requirements.txt  # if requirements are added later
```

## Usage

```python
from divine_agents import Agent, philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

conversation = philosophical_dialogue(alice, bob)
for line in conversation:
    print(line)
```

## Testing

Unit tests verify state transitions and dialogue responses. To run them:

```bash
python -m pytest -q
```
