# Divine-Ascension-System

This project simulates philosophical debates between ontological agents. Each agent can exist in one of three states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents transition between these states when their emotional intensity or tension exceeds certain thresholds. The module `divine_agents` exposes the core classes and functions used for these interactions.

## Running the dialogue

To see a sample conversation, run the dialogue module directly:

```bash
python -m divine_agents.dialogue
```

This command creates two agents and prints a short exchange demonstrating state transitions and responses. You can also import the package and construct your own agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")
for line in philosophical_dialogue(alice, bob):
    print(line)
```

## Running the tests

All tests are written using `unittest`. Execute them from the repository root with:

```bash
python -m unittest discover -s tests
```

## Dependencies

The project requires **Python 3.8** or newer and uses only the Python standard library. No additional packages are needed.
