# Divine-Ascension-System

This project simulates a set of philosophical agents that evolve through three ontological states: **Ego**, **Jaz**, and **Enotnost**. Each agent tracks its emotional intensity and tension; once tension exceeds `0.7` or emotion exceeds `0.5`, the agent moves to the next state.

* **Ego** – truth is absolute and independent.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents debate questions of absolute, relative, and unified truth. Their emotional state influences their answers and may trigger a transition to a new state.

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Running the philosophical dialogue

The `philosophical_dialogue` function engages two agents in conversation and demonstrates automatic state transitions.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running the script will display each agent's view of truth and any state changes.

## Testing

Unit tests ensure correct transitions and responses. Execute them with:

```bash
python -m unittest discover -s tests
```


