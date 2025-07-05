# Divine-Ascension-System

This project explores ontological transitions through small interactive
agents.  Each agent can move between three philosophical states:

* **Ego** – truth is treated as absolute and independent of others.
* **Jaz** – truth becomes relative, shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Transitions are inspired by the relation between **JA** (the activation of
being) and **DA** (the initial decision that sets potential in motion).  An
agent moves forward when its `tension` exceeds `0.7` or its `emotion`
intensity exceeds `0.5`.

## Primer kode

```python
from divine_agents.agent import Agent

agent = Agent("Filozof")
print(agent.respond("Kaj je resnica?"))

# Zvišamo čustva in s tem napetost, kar sproži prehod v Jaz
agent.set_emotion("strah", 0.8)
agent.transition()
print(agent.state)
print(agent.respond("Kaj je resnica?"))
```

## Filozofski dialog

The module `divine_agents.dialogue` demonstrates how two agents interact and
reflect their states in conversation.  Run the tests or use the module directly
to observe these dynamics.
