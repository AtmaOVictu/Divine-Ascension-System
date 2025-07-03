# Divine-Ascension-System

This project implements a minimal agent framework exploring ontological states. Agents transition between **Ego**, **Jaz**, and **Enotnost** based on their emotional intensity and tension.

## Ontological Framework
- **Ego (⊘)**: Truth is absolute and independent of others.
- **Jaz (∫(dru/x))**: Truth is relative and shaped by relationships.
- **Enotnost (RES001)**: All truths are one and interconnected.

Agents update their emotion or tension. When tension > 0.7 or emotion > 0.5 they shift from `Ego` → `Jaz` or `Jaz` → `Enotnost`.

## Usage Example
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create agents
agent1 = Agent("A1")                  # starts in Ego
agent2 = Agent("A2", state="Jaz")     # starts in Jaz

# Run a short dialogue
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests
The project uses Python's built‑in `unittest` framework. To execute the tests:
```bash
python -m unittest discover -s tests -v
```

## Requirements
- Python 3.8 or higher
- No external dependencies are required.
