# Divine-Ascension-System

This project simulates philosophical agents that evolve through three ontological states:

- **Ego** – truth is absolute and personal.
- **Jaz** – truth is relative and defined through relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents hold a *tension* and an *emotion* value. When `tension` exceeds `0.7` or `emotion` is above `0.5`, they transition from **Ego** ➜ **Jaz** or **Jaz** ➜ **Enotnost**. Dialogue between agents reflects their current state and emotional intensity.

## Dialogue Mechanics

The `philosophical_dialogue` function demonstrates how two agents interact. Each agent replies according to its state, updates its emotion, and may transition if the defined thresholds are reached.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies (there are none outside the standard library, but a requirements file is provided for completeness):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the unit tests:
   ```bash
   python -m unittest discover tests
   ```

## Quick Start Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")              # starts in Ego
agent2 = Agent("A2", state="Jaz")  # starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This snippet creates two agents and prints a short dialogue demonstrating state transitions and philosophical responses.
