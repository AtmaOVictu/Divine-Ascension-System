# Divine-Ascension-System

This project demonstrates a simple ontological agent system implemented in Python.
Agents can transition between philosophical states (``Ego``, ``Jaz`` and ``Enotnost``)
based on their emotional level and tension.

## Installation

Clone the repository and ensure you have Python 3.11 or later available:

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

There are no external dependencies, so the system can be used immediately.

## Example usage

Create a couple of agents and let them debate using the provided dialogue
function:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")  # defaults to the Ego state
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script will show how each agent responds and transitions between
states during the conversation.

## Running tests

Execute the unit tests with ``pytest`` from the project root:

```bash
python -m pytest -q
```

The tests verify state transitions, agent responses and the dialogue flow.
