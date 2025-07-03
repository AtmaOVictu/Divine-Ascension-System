# Divine-Ascension-System

This project implements a small agent framework for exploring philosophical
dialogue. The main classes and helpers can be imported directly from the
``divine_agents`` package.

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

