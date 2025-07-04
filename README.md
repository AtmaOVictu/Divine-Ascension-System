# Divine-Ascension-System

## Project Overview

Divine-Ascension-System is a **heavyweight** framework for simulating philosophical agents. Each
agent can occupy one of three ontological states—**Ego**, **Jaz**, or
**Enotnost**—and transitions between these states are triggered by the
agent's emotions and tension. The library also provides tools for generating
dialogues in which agents debate absolute, relative and unified truths.

## Installation

Clone this repository and install the package in editable mode or export the
repository directory on your `PYTHONPATH`:

```bash
git clone <repo-url>
cd Divine-Ascension-System
pip install -e .  # optional; alternatively export PYTHONPATH=.
```

## Running Tests

Unit tests ensure that state transitions and dialogue generation behave as
expected. Run all tests with:

```bash
PYTHONPATH=. pytest
```

## Example Usage

The `philosophical_dialogue` function lets two agents debate truth from their
current perspectives. A minimal example:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running the snippet prints each agent's answers and shows how their states
change as emotions and tension rise.
