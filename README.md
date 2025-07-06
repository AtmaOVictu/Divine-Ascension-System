# Divine-Ascension-System

This project simulates philosophical debates between ontological agents. Each
agent transitions through states **Ego**, **Jaz** and **Enotnost** depending on
their emotion and tension levels.

## Running the dialogue

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running tests

Execute the unit tests with:

```bash
python -m unittest discover tests
```
