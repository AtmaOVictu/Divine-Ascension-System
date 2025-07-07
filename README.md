# Divine-Ascension-System

This project demonstrates a minimal agent-based framework for exploring
philosophical ideas. Agents transition through ontological states and engage in
dialogue influenced by their emotional levels.

## Setup

The code requires Python 3.11+. No external dependencies are needed. To run the
unit tests use:

```bash
python -m pytest -q
```

Running plain `pytest` also works after installing the package in editable mode
or using the included `tests/__init__.py` file.

## Example Dialogue

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

The agents will discuss truth, adjust their emotions and potentially transition
to new states during the conversation.
