# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Logging transitions

You can record state changes of an agent by providing a path to
`transition`.

```python
from divine_agents.agent import Agent

agent = Agent("Janez")
log_file = "history.log"
agent.update_tension(0.8)
agent.transition(log_file)  # writes current state with timestamp
```
