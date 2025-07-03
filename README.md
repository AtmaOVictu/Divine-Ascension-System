# Divine-Ascension-System

A small library showcasing ontological agents that transition between philosophical states based on emotion and tension. Agents debate absolute, relative, and unified truths through dialogue.

## Usage

Create agents and run a dialogue simulation:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Install `pytest` and execute the test suite from the repository root:

```bash
python -m pytest
```

## Requirements

- Python 3.8 or newer
- pytest (for running tests)
