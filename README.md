# Divine-Ascension-System

This project explores agent interactions using an ontological framework. Agents move between three states based on their emotions and tension levels:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are one and interconnected.

The system simulates dialogue where agents discuss philosophical ideas and transition between states when tension exceeds 0.7 or emotion exceeds 0.5.

## Setup

1. Ensure you have **Python 3.8+** installed.
2. Install dependencies (none required beyond the standard library).

## Running Tests

Use the built‑in test suite to verify state transitions and dialogue responses:

```bash
python -m unittest
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents in different initial states
agent1 = Agent("A1")                      # starts in Ego
agent2 = Agent("A2", state="Jaz")         # starts in Jaz

# Run a short dialogue and print the lines
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This will output each agent's philosophical perspective and show how their
states may change according to their emotions and tension.
