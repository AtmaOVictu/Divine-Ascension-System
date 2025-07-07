# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

This package exposes a small framework for creating ontological agents and
letting them debate their view of truth.

## Usage

Import the convenience exports from :mod:`divine_agents` and run a dialogue:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

The function returns a list of dialogue lines which can be printed or further
processed.
