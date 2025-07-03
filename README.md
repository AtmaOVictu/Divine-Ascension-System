# Divine-Ascension-System

This project provides a minimal framework for philosophical agents that evolve through three ontological states:

- **Ego**: truth is absolute and independent.
- **Jaz**: truth is relative and shaped by relations.
- **Enotnost**: all truths are interconnected and unified.

Agents adjust their emotional tension and can transition between these states during philosophical debates.

## Installation

The package can be installed directly from the repository with `pip`:

```bash
pip install git+https://github.com/<username>/Divine-Ascension-System.git
```

Alternatively, after cloning the repository you can install it in editable mode:

```bash
pip install -e .
```

## Running Tests

The project includes unit tests located in the `tests` directory. Run them with:

```bash
python -m unittest discover tests
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

This snippet creates two agents and performs a short dialogue demonstrating state transitions and philosophical responses.
