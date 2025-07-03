# Divine-Ascension-System

This repository contains a minimal agent system used to explore
philosophical debates. Agents move between ontological states
(*Ego*, *Jaz*, *Enotnost*) based on their emotional and tension levels.
The package exposes utilities to create agents, trigger state transitions
and run sample dialogues.

## Running tests

Execute the unit tests with the standard Python test runner:

```bash
python -m unittest
```

## Example usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Repository structure

- `divine_agents/` – core modules implementing agents and dialogues.
- `tests/` – unit tests verifying transitions and responses.
