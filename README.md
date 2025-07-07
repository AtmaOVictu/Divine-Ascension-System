# Divine-Ascension-System

This project models dynamic philosophical agents transitioning between states based on tension and emotion. Agents debate absolute, relative and unified truth while their feelings shape the conversation.

## Setup
1. No external dependencies are required.
2. Run tests with `pytest`:
   ```bash
   pytest -q
   ```

## Usage Example
Use the `Agent` class and `philosophical_dialogue` function to start a short exchange:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
