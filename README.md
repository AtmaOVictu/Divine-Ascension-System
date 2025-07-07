# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Dynamic Debate

The library provides simple ontological agents that can change states based on
their emotional tension. Use `dynamic_debate` to run a short conversation where
emotions escalate and trigger transitions:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_debate

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
lines = dynamic_debate(a1, a2, rounds=3)
for line in lines:
    print(line)
```
