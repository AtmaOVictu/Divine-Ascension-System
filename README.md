# Divine-Ascension-System

The Divine Ascension System provides a small framework for experimenting with
ontological agents. Each agent moves between the **Ego**, **Jaz** and
**Enotnost** states according to its emotional level and tension. The project
includes helpers to create dialogues where agents debate the nature of truth
from these different philosophical viewpoints.

## Running Tests

Unit tests are located in the `tests` directory. They can be executed with

```bash
python -m pytest
```

Running the tests verifies state transitions and dialogue behaviour.

## Usage Example

Create a few agents and run a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

This will produce output demonstrating how the agents transition between states
and respond based on their current philosophical perspective.
