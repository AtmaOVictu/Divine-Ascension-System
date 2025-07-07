# Divine-Ascension-System

This project demonstrates a simple agent-based framework inspired by ontological philosophy. Agents can be in one of three states:

- **Ego** – truth is absolute and independent.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and connected.

Each agent tracks `tension` and `emotion`. If tension exceeds `0.7` or emotion exceeds `0.5`, the agent transitions from **Ego** to **Jaz** or from **Jaz** to **Enotnost**. Dialogue between agents shows how their philosophical responses evolve as their states change.

## Running the dialogue module

Launch a Python session and invoke the dialogue function:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```

This will print a short conversation and display any state transitions.

## Running tests

Unit tests are located in the `tests` directory. Execute them with:

```bash
python -m unittest discover -s tests
```

This command runs all tests in the suite and verifies agent transitions and dialogue responses.
