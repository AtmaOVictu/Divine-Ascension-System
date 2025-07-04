# Divine Ascension System

This project demonstrates a minimal ontological framework where agents evolve
through three philosophical states: **Ego**, **Jaz**, and **Enotnost**. Each
agent is influenced by emotion and tension which may trigger state transitions.

## Installation

```bash
pip install -e .
```

## Running Tests

Execute the unit tests with:

```bash
python -m pytest -q
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2, emotions=[(0.8, 0.6)]):
    print(line)
```

The dialogue illustrates how agents update their emotional state and progress
through the ontological phases.
