# Divine-Ascension-System

This project implements a set of philosophical agents that can shift between ontological states based on their emotional intensity and tension. Agents debate absolute, relative and unified truths as they move from **Ego** to **Jaz** and finally **Enotnost**.

## Installation

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt  # if a requirements file exists
```

## Usage

Agents can be created and run through the provided dialogue utilities:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Testing

Run the unit tests with:

```bash
pytest
```

The tests verify state transitions triggered by emotion or tension and ensure responses align with the agent's ontological state.
