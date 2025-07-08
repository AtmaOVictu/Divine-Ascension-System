# Divine-Ascension-System

This repository implements a minimal agent framework used for experimenting
with ontological state transitions and philosophical dialogues. Each agent can
shift from **Ego** to **Jaz** to **Enotnost** based on its current tension or
emotional intensity. A lightweight `KnowledgeBase` tracks which concepts have
already been explored so agents avoid unnecessary repetition.

Basic usage:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
conversation = philosophical_dialogue(a1, a2)
for line in conversation:
    print(line)
```

Unit tests demonstrating state transitions and knowledge tracking are provided
in the `tests` directory.
