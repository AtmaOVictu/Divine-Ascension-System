# Divine-Ascension-System

This project provides a small framework for experimenting with ontological agents.

## Agent
`Agent` represents a being that can move through three ontological states: **Ego**, **Jaz**, and **Enotnost**. Each agent keeps track of its current `state`, `tension`, and `emotion`. When the tension rises above `0.7` or the emotion intensity is above `0.5`, the agent transitions to the next state. The agent's `respond` method answers a philosophical question according to this state.

## philosophical_dialogue
`philosophical_dialogue` simulates a short conversation between two agents. It has each agent answer a question, raises their emotion (which can trigger a state transition), and then has them answer again from their new perspective.

## Example
Create two agents and let them converse:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

if __name__ == "__main__":
    a1 = Agent("A1")
    a2 = Agent("A2", state="Jaz")
    for line in philosophical_dialogue(a1, a2):
        print(line)
```

Run the script with `python example.py` to see the dialogue and transitions.

## Running tests
Install any dependencies and run the unit tests with:

```bash
PYTHONPATH=. pytest
```

These tests verify state transitions, responses, and the dialogue output.
