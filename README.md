# Divine-Ascension-System

This project implements a small agent based system exploring ontological
philosophy. Agents transition between the states **Ego**, **Jaz** and
**Enotnost** as their emotions and tension rise. Each state influences the
philosophical position expressed by the agent.

## Running a Dialogue

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running Tests

Execute all tests with:

```bash
python -m unittest discover tests
```
