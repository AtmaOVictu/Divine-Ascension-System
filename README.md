# Divine Ascension System

This project models a set of ontological agents that transition between three
philosophical states: **Ego**, **Jaz**, and **Enotnost**. Agents hold emotion and
tension values which influence their evolution and responses during dialogue.

## Usage

Install requirements (none beyond the Python standard library) and import the
main classes:

```python
from divine_agents import Agent, OntologyState, philosophical_dialogue
```

Create agents and run a dialogue:

```python
agent1 = Agent("A1")
agent2 = Agent("A2", state=OntologyState.JAZ)

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Unit tests verify state transitions, dialogue output and extreme condition
handling. Execute them with:

```bash
python -m unittest
```

