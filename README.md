# Divine-Ascension-System

The Divine-Ascension-System is a small Python project that explores how agents
move through philosophical states based on their emotions and tension. Each
agent can transition from **Ego** to **Jaz** and finally to **Enotnost** as they
experience emotional growth. Dialogues between agents illustrate how their
beliefs about truth change throughout this journey.

## Installation

Clone the repository and install the dependencies with `pip`:

```bash
git clone <repository-url>
cd Divine-Ascension-System
pip install -r requirements.txt
```

## Usage Example

Create two agents and run a short philosophical dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Philosophical Model

Agents embody three ontological states:

1. **Ego** – truth is absolute and independent of others.
2. **Jaz** – truth is relative and shaped by our relationships.
3. **Enotnost** – all truths are unified and interconnected.

An agent transitions to the next state when its `tension` exceeds `0.7` or
its `emotion` exceeds `0.5`. These transitions capture the agent's growing
awareness and emotional maturity.

## Running Tests

Unit tests reside in the `tests` directory. Execute them using:

```bash
python -m pytest
```

The tests verify state transitions and dialogue responses to ensure agents
behave according to the philosophical model.
