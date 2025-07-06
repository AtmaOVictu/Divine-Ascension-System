# Divine-Ascension-System

This project implements ontological agents that evolve through three states:
**Ego**, **Jaz**, and **Enotnost**. Agents change state when their emotional
intensity or tension exceeds set thresholds. They engage in short dialogues to
illustrate different views of truth based on their current state.

## Installation

No external dependencies are required except for `pytest` to run the tests.
Install it with:

```bash
pip install pytest
```

## Usage

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Execute the unit tests with:

```bash
pytest
```

## Ontological States

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are unified and interconnected.

