# Divine Ascension System

This project implements a small agent based framework inspired by philosophical principles.
Agents transition between three ontological states and interact through dialogue.

## Installation
Clone the repository and ensure Python 3.11+ is available.
No external dependencies are required.

## Running Tests
Execute the following command from the project root:

```bash
pytest -q
```

## Usage Example
Create two agents and run a short philosophical conversation:

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

The agents will update their emotions, transition states when thresholds are exceeded, and respond according to their current philosophical view.
