# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Emotional increments

Agents can update their emotion by specifying an emotion type and an increment.

```python
from divine_agents.agent import Agent

agent = Agent("Ada")
agent.apply_emotional_increment("fear", 0.6)
agent.transition()
```

The example above increases Ada's emotion and tension by `0.6`,
potentially triggering a state transition.
