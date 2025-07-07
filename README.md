# Divine-Ascension-System

This project models dynamic philosophical agent interactions with state transitions
based on emotions, tension and ontological principles. Agents move between three
states—**Ego**, **Jaz** and **Enotnost**—and generate dialogue reflecting these
perspectives.

## Setup Instructions
1. Install dependencies (none outside the standard library).
2. Run tests:
   ```bash
   pytest -q
   ```

## Usage Example
A small dialogue can be created using the `philosophical_dialogue` helper:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
