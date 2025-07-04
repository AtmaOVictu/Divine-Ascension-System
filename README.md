# Divine-Ascension-System

The **Divine Ascension System** is a minimal agent-based framework for simulating philosophical debates. Agents transition between the ontological states **Ego**, **Jaz**, and **Enotnost** based on their tension and emotions. Their responses reflect different understandings of truth:

- **Ego**: truth is absolute and independent of others.
- **Jaz**: truth is relative and shaped by relationships.
- **Enotnost**: all truths are unified and interconnected.

Agents update their emotional state during conversations which may trigger state transitions. The included dialogue helpers make it easy to demonstrate these interactions.

## Setup

This project requires **Python 3.8+** and has no external dependencies. Clone the repository and (optionally) create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Running tests

Execute the unit tests with Python's built‑in `unittest` module:

```bash
python -m unittest discover tests
```

## Example usage

Below is a short example that creates two agents and runs a dialogue between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script will show each agent's initial answer about truth, followed by any state transitions and their responses in the new state.
