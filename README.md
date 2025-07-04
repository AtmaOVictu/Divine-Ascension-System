# Divine-Ascension-System

This project simulates philosophical agents that evolve through three ontological states: **Ego**, **Jaz**, and **Enotnost**. Each transition is influenced by an agent's emotion and tension levels.

## Installation

```bash
# clone the repository
git clone https://github.com/yourname/Divine-Ascension-System.git
cd Divine-Ascension-System

# optional: create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
```

This project has no external dependencies, but a virtual environment keeps your Python packages isolated.

## Running the `philosophical_dialogue` example

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# create two agents
agent1 = Agent('Agent 1')
agent2 = Agent('Agent 2', state='Jaz')

for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

The script prints a short conversation where both agents discuss the nature of truth and may change their ontological state depending on their emotions.

## Running unit tests

Make sure `pytest` is installed and run the tests from the repository root:

```bash
pip install pytest  # if not already installed
PYTHONPATH=. python -m pytest
```

## Ontological states and transitions

Agents move through the following states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are one and interconnected.

During a dialogue, an agent transitions from **Ego** to **Jaz** or from **Jaz** to **Enotnost** when its tension exceeds `0.7` or its emotion surpasses `0.5`.
