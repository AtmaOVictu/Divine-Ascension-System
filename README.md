# Divine-Ascension-System

This project contains a small agent framework used to model ontological
conversations. Agents transition through the states **Ego**, **Jaz** and
**Enotnost** based on their emotions and tension. A dialogue simulation is
provided to showcase how agents move between these philosophical points of view.

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
