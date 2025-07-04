# Divine-Ascension-System

## Project Overview

Divine-Ascension-System is a lightweight framework for simulating philosophical agents. Agents
occupy one of three ontological states—**Ego**, **Jaz**, or **Enotnost**—and can transition
between these states when their emotion or tension exceeds defined thresholds. The
library also provides utilities for generating dialogues where agents debate absolute,
relative and unified truths.

## Installation

Clone this repository and either install it in editable mode or export the repository
path on your `PYTHONPATH`:

```bash
git clone <repo-url>
cd Divine-Ascension-System
pip install -e .  # optional; alternatively export PYTHONPATH=.
```

## Running Tests

Unit tests verify that state transitions and dialogue generation behave as expected.
Execute them with:

```bash
PYTHONPATH=. pytest
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

Running this code prints each agent's answers and shows how their states change as
emotions and tension rise during the discussion.
