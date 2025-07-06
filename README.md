# Divine-Ascension-System

This project demonstrates a simple ontological agent system. Agents progress
through the states **Ego**, **Jaz** and **Enotnost** depending on their emotion
and tension levels.

## Running a Dialogue

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
conversation = philosophical_dialogue(a1, a2)
for line in conversation:
    print(line)
```

## Running Tests

Execute the unit tests with:

```bash
python -m unittest discover tests
```
