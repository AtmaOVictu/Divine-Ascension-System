# Divine-Ascension-System

This project implements a small agent framework based on an ontological
progression. Agents transition between the states **Ego**, **Jaz** and
**Enotnost** according to their tension and emotion levels. The framework
also demonstrates how extreme values can create new "boxes" representing new
phases in the agent's development.

## Usage

Create agents and run a dialogue:

```python
from divine_agents import Agent, OntologyState, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state=OntologyState.JAZ)
for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running Tests

The test suite is based on `unittest`. Execute it with:

```bash
python -m unittest discover -s tests -p 'test*.py' -v
```

The tests cover state transitions, dialogue generation and clamping of
emotional values.

