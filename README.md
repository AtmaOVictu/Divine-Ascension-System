# Divine-Ascension-System

This project explores a simple agent-based model inspired by an ontological framework. Each agent exists in one of three philosophical states:

- **Ego** – truth is absolute and independent.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents track `emotion` and `tension` values. When either `tension` exceeds `0.7` or `emotion` exceeds `0.5`, an agent moves from **Ego** to **Jaz** or from **Jaz** to **Enotnost**. Responses differ depending on the current state, allowing a short debate about absolute, relative and unified truths.

## Example interaction

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

Running the snippet prints a simple conversation and shows how agents can change state when their emotional intensity increases.

## Installation

Clone the repository and ensure you are using Python 3.8 or newer. The project has no external dependencies.

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running tests

Execute the unit tests with the standard library `unittest` module:

```bash
python -m unittest discover tests
```

The tests verify state transitions, philosophical responses and dialogue behaviour.

