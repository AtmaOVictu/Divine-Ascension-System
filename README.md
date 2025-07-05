# Divine-Ascension-System

A dynamic agent-based framework for exploring philosophical debates through
ontological state transitions. Agents move between **Ego**, **Jaz**, and
**Enotnost** depending on their emotional intensity and tension. The library
includes simple tools to simulate dialogues and observe how philosophy and
emotion shape each agent's view of truth.

## Running the tests

Use `python -m pytest -q` from the repository root:

```bash
python -m pytest -q
```

## Example usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents in different states
alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```
