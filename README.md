# Divine-Ascension-System

This project provides a small agent framework used to explore
philosophical dialogues. Agents start in states such as **Ego**, **Jaz** or
**Enotnost** and can transition when their emotional intensity or tension is
high enough. The accompanying module includes a helper function to simulate a
short exchange where agents reason about absolute, relative and unified truths.

## Running Tests

Tests require `pytest`. Execute them from the repository root so the package can
be discovered:

```bash
PYTHONPATH=. pytest -q
```

All tests should pass and demonstrate the expected state transitions and
responses.

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

Running this snippet will show a brief dialogue and the resulting state
changes.
