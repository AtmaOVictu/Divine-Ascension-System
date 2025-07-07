# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Usage

Create agents and let them discuss philosophical truths:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

This will print a short dialogue showing each agent's view of truth and any
state transitions triggered by their emotions.

## Running Tests

Ensure all unit tests pass by running:

```bash
python -m unittest
```

The tests verify state transitions, responses, and the generated dialogue.
