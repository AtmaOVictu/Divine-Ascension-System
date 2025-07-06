# Divine-Ascension-System

A small framework for simulating philosophical agents. Agents transition
through the states **Ego**, **Jaz**, and **Enotnost** based on their
emotion and tension. Use the provided utilities to create debates and
observe how emotional intensity changes an agent's view on truth.

Example:

```python
from divine_agents import Agent, Conversation

# prepare agents
ego = Agent("Egoist")
relativist = Agent("Relativist", state="Jaz")

# run a short debate
conv = Conversation(ego, relativist)
conv.run(rounds=1, emotions1=[0.8], emotions2=[0.6])
print(conv.history)
```
```
['Egoist (Ego): Resnica je absolutna in neodvisna od drugih.',
 'Relativist (Jaz): Resnica je relativna, oblikovana z našimi odnosi.']
```
