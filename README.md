# Divine-Ascension-System

This project contains a small framework for experimenting with
**ontological agents**. Each agent can exist in one of three
philosophical states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents transition between these states when their tension exceeds `0.7`
or their emotional level exceeds `0.5`. The `dialogue` module provides a
simple conversation demonstrating how emotions can trigger transitions
and alter the agents' responses.

## Example usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")               # starts in Ego
a2 = Agent("A2", state="Jaz")  # starts in Jaz

for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running the tests

The repository includes a small test-suite. Execute it from the project
root using:

```bash
python -m pytest -q
```
