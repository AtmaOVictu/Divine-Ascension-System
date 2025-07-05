# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Saving and Loading Agents

Agents can persist their internal state and history to a JSON file. This makes
it possible to resume a dialogue later.

```python
from divine_agents import Agent

agent = Agent("A1", state="Jaz")
agent.update_emotion(0.8)
agent.transition()
agent.save("agent.json")

loaded = Agent.load("agent.json")
print(loaded.state)
```
