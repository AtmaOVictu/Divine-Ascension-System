# Divine-Ascension-System

Divine-Ascension-System is a small framework for simulating ontological agents.
Agents progress through three philosophical states:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by our relationships.
- **Enotnost** – All truths are unified and interconnected.

Agent state transitions depend on their emotional intensity and tension level.
This repository includes basic agent definitions, simple dialogue simulation,
and tests demonstrating how agents evolve.

## Installation

The project has no external dependencies beyond Python 3. Clone the repository
and optionally create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install any development requirements (only `pytest` is needed for tests):

```bash
pip install pytest
```

## Running Tests

Execute the test suite from the repository root. Because the package is not
installed, set the `PYTHONPATH` so tests can import the source modules:

```bash
PYTHONPATH=. pytest
```

All tests should pass and demonstrate state transitions and basic dialogue
behaviour.

## Usage Example

Create agents and run a short philosophical exchange:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

Running this code will show how each agent responds based on its ontological
state, updates its emotion and tension, and possibly changes state during the
conversation.
