# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

This project simulates philosophical agents that transition between ontological
states based on their emotional tension. Agents begin in **Ego**, may progress
to **Jaz**, and finally to **Enotnost** when their tension or emotion crosses
predefined thresholds.

Example usage:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
lines = philosophical_dialogue(a1, a2)
for l in lines:
    print(l)
```

Run tests with `pytest` to verify behaviour.
