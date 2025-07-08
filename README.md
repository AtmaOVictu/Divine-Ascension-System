# Divine-Ascension-System

This project demonstrates a simple ontological agent framework. Agents can
transition through three philosophical states based on their emotions and
tension levels:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are one and interconnected.

## Creating Agents

```python
from divine_agents.agent import Agent

# create an agent in the default `Ego` state
agent = Agent("A1")
print(agent.state)  # -> "Ego"

# adjust emotion or tension to trigger transitions
agent.update_emotion(0.8)
agent.transition()  # -> "Jaz"
```

## Starting a Dialogue

Use `philosophical_dialogue` to run a short exchange between two agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running the Tests

Install the project dependencies (none besides Python itself) and run the test
suite:

```bash
python -m pytest
```

If you encounter import errors when using the `pytest` command directly, run:

```bash
pytest -q
```

All tests should pass, confirming that state transitions and dialogues behave as
expected.
