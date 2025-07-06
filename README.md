# Divine-Ascension-System

Simple simulation of ontological agents that transition between the states
**Ego**, **Jaz** and **Enotnost**.  Transitions are triggered by tension or
emotion levels.  Agents can engage in short dialogues about the nature of
truth.

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

Execute `pytest` from the repository root to run the unit tests.
