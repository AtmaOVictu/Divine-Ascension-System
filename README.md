# Divine-Ascension-System

A modular framework for simulating philosophical agents. Each agent transitions between the **Ego**, **Jaz**, and **Enotnost** states based on emotion and tension while engaging in dialogue about absolute, relative, and unified truths.

## Installation

Clone the repository and install in editable mode:

```bash
pip install -e .
```

## Usage

Create agents and run a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")  # defaults to Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

The conversation will show how each agent responds according to their current state and how they transition when emotion or tension thresholds are exceeded.

## Running Tests

Execute the unit test suite with:

```bash
python -m unittest discover tests
```
