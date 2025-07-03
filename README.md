# Divine-Ascension-System

The **Divine-Ascension-System** simulates dialogues between ontological agents.
Agents transition through three philosophical states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are one and interconnected.

Agents update their emotional intensity and tension during conversations.
When tension exceeds `0.7` or emotion exceeds `0.5`, an agent may move
from **Ego** to **Jaz**, or from **Jaz** to **Enotnost**.

## Running an Example Dialogue

Use the `divine_agents` package to create agents and run a sample dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This prints lines showing each agent's responses and any state transitions.

## Running the Unit Tests

To execute the unit tests, ensure the package is discoverable and run
pytest from the repository root:

```bash
PYTHONPATH=. python -m pytest -q
```

All tests should pass and confirm that state transitions and dialogue
responses behave as expected.
