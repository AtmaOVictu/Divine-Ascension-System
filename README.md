# Divine-Ascension-System

This project provides a simple framework for simulating ontological agents
that evolve through three philosophical states: **Ego**, **Jaz**, and
**Enotnost**.  State transitions are triggered by tension and emotions.

An example utility `ionize_word` demonstrates how text can be transformed by
shifting each character by one in the ASCII table:

```python
>>> from divine_agents.ionize import ionize_word
>>> ionize_word("beseda")
'cftfeb'
```

To initiate a dialogue between two agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```
