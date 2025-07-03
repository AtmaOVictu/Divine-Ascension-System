# Divine-Ascension-System
Example usage of the ontological agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

Run unit tests with:

```bash
pytest -q
```
