# Divine Agents: Ontological Agent Simulation

This project models agents that progress through philosophical states of **Ego**, **Jaz**, and **Enotnost**. Agents transition when their tension or emotion exceed defined thresholds, and they respond to questions according to their current ontological understanding of truth.

## Setup

Clone the repository and install the package in editable mode:

```bash
git clone <repository-url>
cd Divine-Ascension-System
python -m pip install -e .
```

## Usage

Create two agents and simulate a short dialogue:

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Run the unit tests with:

```bash
python -m unittest
```

## Philosophy

* **Ego** – Truth is absolute and independent.
* **Jaz** – Truth is relative and shaped by relationships.
* **Enotnost** – All truths are unified and interconnected.

