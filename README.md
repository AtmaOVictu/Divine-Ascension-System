# Divine-Ascension-System

This project explores philosophical dialogue through a small agent-based simulation. Agents transition between ontological states and respond to each other based on emotions and tension levels.

## Philosophical Agent System
Agents can be in one of three states:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships.
- **Enotnost** – All truths are unified and interconnected.

Each agent tracks its current state, emotional intensity, and tension. If an agent's tension rises above `0.7` or emotion above `0.5`, it will transition:

1. `Ego` → `Jaz`
2. `Jaz` → `Enotnost`

The `Agent` class exposes `update_emotion`, `update_tension`, `transition`, and `respond` methods to manage these interactions.

## Installation
1. Ensure Python 3 is available on your system.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests
Execute the unit tests with `pytest`:

```bash
python -m pytest -q
```

## Example Dialogue
The snippet below creates two agents, runs a simple dialogue, and prints the lines of conversation:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This will output a short exchange where each agent responds according to its state and may transition when emotion or tension thresholds are reached.
