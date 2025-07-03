# Divine-Ascension-System

This project provides a small agent-based framework where agents move between ontological states and converse about truth. Each agent carries a **state**, a level of **tension**, and an **emotion** value. When emotion exceeds `0.5` or tension exceeds `0.7`, the agent transitions from `Ego` to `Jaz` or from `Jaz` to `Enotnost`.

## Ontological States

- **Ego** – Truth is considered **absolute** and independent of others.
- **Jaz** – Truth is **relative**, shaped by relationships and interactions.
- **Enotnost** – Truth is **unified** and all truths are interconnected.

## Setup

The library only relies on the Python standard library. Clone the repository and ensure you have Python 3.8+ installed.

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running a Dialogue

Create two agents and run a short philosophical conversation:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")  # starts in Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This script shows how an agent may change state when its emotion or tension surpasses the thresholds and how each state influences the responses.

## Running the Unit Tests

The project includes unit tests under the `tests/` directory. Run them with Python's builtin test runner:

```bash
python -m unittest discover -s tests
```

The tests verify correct state transitions and the philosophical dialogue.
