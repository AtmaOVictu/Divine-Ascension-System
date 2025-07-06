# Divine-Ascension-System

This project provides a small framework for experimenting with ontological agents. An agent can exist in one of three philosophical states—**Ego**, **Jaz**, or **Enotnost**—and transitions between them depend on the agent's current emotion and tension levels. Agents can engage in short philosophical dialogues demonstrating how their states influence their perception of truth.

## Installation

The project uses a minimal `pyproject.toml` configuration so it can be installed in editable mode. From the repository root run:

```bash
python -m pip install -e .
```

## Running Tests

All unit tests are located in the `tests` directory. You can run them with either `pytest` or the built‑in unittest module:

```bash
pytest
# or
python -m unittest
```

## Basic Usage

Create individual agents and run a dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# two agents starting in different states
agent1 = Agent("A1")          # defaults to Ego
agent2 = Agent("A2", state="Jaz")

# run a short philosophical exchange
lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

The output demonstrates how each agent transitions from **Ego** to **Jaz** or from **Jaz** to **Enotnost** when emotion or tension thresholds are exceeded.
