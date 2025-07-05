# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Overview

This project simulates ontological agents that transition between the states
**Ego**, **Jaz**, and **Enotnost**. Transitions are governed by emotion and tension
thresholds defined in `Legitimator`.

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```
