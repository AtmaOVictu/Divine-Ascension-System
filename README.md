# Divine-Ascension-System

This project implements a small simulation of ontological agents that can move
between three philosophical states: **Ego**, **Jaz** and **Enotnost**. An agent
changes state when its tension rises above `0.7` or its emotion rises above
`0.5`. Each state represents a different view of truth:

- **Ego** – truth is absolute and independent.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and connected.

## Installation

The project has no external dependencies. Simply clone the repository and run
the tests to verify the environment:

```bash
pip install -r requirements.txt  # (optional, there are currently no deps)
```

## Usage

Create a pair of agents and start a philosophical discussion:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

first = Agent("A1")
second = Agent("A2", state="Jaz")
for line in philosophical_dialogue(first, second):
    print(line)
```

## Testing

Run all unit tests with:

```bash
pytest
```

The tests cover state transitions, agent responses and dialogue behaviour.
