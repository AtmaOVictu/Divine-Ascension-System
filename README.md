# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Dialogue Parameters

The `philosophical_dialogue` function can now be customised with explicit
emotion and tension values for both agents:

```python
from divine_agents.dialogue import philosophical_dialogue

lines = philosophical_dialogue(agent1, agent2,
                               emotion1=0.8, tension1=0.0,
                               emotion2=0.6, tension2=0.0)
```

These parameters influence state transitions during the conversation. Higher
emotion or tension may shift an agent from **Ego** to **Jaz** or from **Jaz** to
**Enotnost** when the thresholds are met.
