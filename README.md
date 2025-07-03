# Divine-Ascension-System

A minimal ontological framework for experimenting with agent-based philosophical dialogue.

## Installation

```bash
# clone the repository
git clone <repository-url>
cd Divine-Ascension-System

# use Python 3.9+
python --version

# there are no external dependencies; the standard library suffices
```

## Running Unit Tests

From the project root run:

```bash
python -m unittest discover -s tests -v
```

This executes the unit tests located in the `tests/` directory.

## Agent Philosophy

Agents exist in one of three states:

- **Ego** — truth is absolute and independent of others.
- **Jaz** — truth is relative and formed by relationships.
- **Enotnost** — all truths are unified and interconnected.

Tension (>0.7) or emotion (>0.5) can move an agent from **Ego** to **Jaz**, and from **Jaz** to **Enotnost**.

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")             # starts in Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This snippet demonstrates two agents debating the nature of truth and automatically transitioning states when emotional intensity is high.
