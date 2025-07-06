# Divine-Ascension-System

Simple framework for simulating philosophical agents.

## Usage

Agents transition between ontological states based on their emotional
intensity or tension. Use the `debate` function to simulate a short
conversation:

```python
from divine_agents import Agent, debate

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in debate(agent1, agent2, turns=2):
    print(line)
```

Unit tests ensure that state transitions and responses behave as
expected.
