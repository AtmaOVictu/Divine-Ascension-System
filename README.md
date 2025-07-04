# Divine-Ascension-System

This project implements a small agent-based framework for experimenting with ontological 
state transitions and philosophical dialogue. Agents shift between the states **Ego**, 
**Jaz**, and **Enotnost** depending on their emotional intensity and tension. Each state 
represents a different view of truth:

* **Ego** – Truth is absolute and independent of others.
* **Jaz** – Truth is relative, shaped by relationships.
* **Enotnost** – All truths are unified and interconnected.

## Installation

Clone the repository and install the package in editable mode:

```bash
pip install -e .
```

## Usage

Agents can interact through the `philosophical_dialogue` helper:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent_a = Agent("A1")
agent_b = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent_a, agent_b):
    print(line)
```

## Running Tests

Run the unit tests with `pytest`:

```bash
pytest -q
```

The tests ensure correct state transitions and dialogue responses.
