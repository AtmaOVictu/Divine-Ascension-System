# Divine-Ascension-System

## Philosophy
The system models agents that can progress through three ontological states:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative, shaped by relationships.
- **Enotnost** – All truths are unified and interconnected.

Agents transition between states when their **tension** is greater than `0.7` or their
**emotion** exceeds `0.5`. Emotions influence both their state and their dialogue
about truth.

## Installation
```bash
pip install -e .
```
This installs the `divine_agents` package in editable mode.

## Example Dialogue
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

