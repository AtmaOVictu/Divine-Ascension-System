# Divine-Ascension-System

This project implements a simple agent framework that explores philosophical state transitions.

## Agent Framework

Agents move through three ontological states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Each agent has `emotion` and `tension` attributes. When tension exceeds `0.7` or emotion exceeds `0.5`, the agent transitions from `Ego` to `Jaz` or from `Jaz` to `Enotnost`. Dialogue helpers allow agents to converse and respond based on their current state.

## Installation

1. Clone this repository.
2. *(Optional)* Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the project dependencies (only `pytest` is required for testing):

```bash
pip install pytest
```

## Running Tests

Execute the unit tests with **pytest** from the repository root:

```bash
python -m pytest
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

