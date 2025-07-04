# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Purpose
This project simulates agents that evolve through ontological states—Ego, Jaz, and Enotnost—according to their emotions and tension. It provides a simple framework for exploring philosophical dialogues where these states influence how agents perceive truth.

## Running the sample dialogue
Run the following snippet to see two agents discuss the nature of truth:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running the tests
Execute the test suite with:

```bash
python -m pytest
```

After Issue 1 is resolved you can also use `pytest` directly.
