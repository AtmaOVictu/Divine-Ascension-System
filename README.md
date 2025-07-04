# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Logging Transitions

```python
from divine_agents.agent import Agent

agent = Agent("A")
agent.update_tension(0.8)
agent.transition(log_path="history.log")
```

The call to `transition` records the agent's new state in `history.log` with a timestamp.
