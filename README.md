# Divine-Ascension-System

This project implements agents that transition between ontological states—**Ego**, **Jaz**, and **Enotnost**—based on their tension and emotion levels. Agents discuss philosophical notions of absolute, relative, and unified truth.

## Installation

```bash
pip install -r requirements.txt  # if you have external dependencies
```

## Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

## Testing

Run unit tests with:

```bash
pytest
```

