# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Usage

You can import the main objects directly from the package root:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```
