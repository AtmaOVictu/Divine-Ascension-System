# Divine-Ascension-System

A minimal framework for experimenting with philosophical agents. Each agent can move through ontological states—**Ego**, **Jaz**, and **Enotnost**—based on emotion and tension. The project demonstrates how agents debate absolute, relative, and unified truths.

## Installation

Clone the repository and install it locally:

```bash
pip install -e .
```

Running `pip install -e .` uses the `setup.py` configuration to install the package in editable mode.

## Usage Example

```python
from divine_agents import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Project Overview

The system models simple state transitions:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships.
- **Enotnost** – All truths are one and interconnected.

Agents update their `tension` and `emotion`, which may trigger transitions when tension exceeds `0.7` or emotion exceeds `0.5`.

## Testing

Install `pytest` and run the tests:

```bash
pytest -q
```

## Philosophical System

Agents answer questions based on their current ontological state. Dialogue shows how an agent's emotional state and tension affect its views on truth. As agents interact, increased emotion or tension can move them from **Ego** to **Jaz**, or from **Jaz** to **Enotnost**, reflecting a shift from absolute toward unified truth.
