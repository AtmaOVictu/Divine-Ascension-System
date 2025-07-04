# Divine-Ascension-System

This project simulates philosophical agents that evolve through
ontological states. Agents transition between **Ego**, **Jaz**, and
**Enotnost** based on their tension and emotions and can hold short
dialogues illustrating their view of truth.

## Features

- Agents track tension, emotion and ontological state.
- Automatic state transitions when thresholds are exceeded.
- Simple interface to generate philosophical dialogue.
- Unit tests covering transitions and responses.

## Installation

The system has no external dependencies beyond Python 3. To set up a
virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate
pip install -U pip
```

## Running Tests

Execute the unit tests with:

```bash
python -m pytest -q
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

The script creates two agents, simulates a dialogue and prints each
line of the conversation.
