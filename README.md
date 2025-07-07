# Divine-Ascension-System

## Project Overview

Divine-Ascension-System is a simple agent-based framework demonstrating
philosophical state transitions. Agents can shift between **Ego**,
**Jaz**, and **Enotnost** based on their tension and emotional values.
A small dialogue engine showcases how these agents interact about
absolute, relative, and unified truths.

## Installation Prerequisites

- Python 3.8 or higher
- No external libraries are required.

Clone the repository and ensure the project root is on your
`PYTHONPATH` when running examples or tests.

```bash
# clone the repo (if you have not already)
# git clone <repo-url>
cd Divine-Ascension-System
```

## Running Unit Tests

The test suite uses `pytest`. Run it from the project root:

```bash
PYTHONPATH=. pytest -q
```

All tests should pass and confirm that state transitions and dialogue
responses behave as expected.

## Dialogue Simulation Example

To see a sample conversation between two agents, execute:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

This will print a short philosophical debate and show any state
changes that occur due to the emotions applied during the dialogue.

## Notebook Purpose

`TESTI.ipynb` is an empty Jupyter notebook reserved for future
experimentation. You can use it to run interactive dialogue
simulations, explore custom agent behaviours, or extend the system with
new features.
