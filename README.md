# Divine-Ascension-System

`divine_agents` provides a lightweight framework for experimenting with
ontological agents.  Each agent can be in one of three states—**Ego**,
**Jaz**, or **Enotnost**—and moves between them when emotion or tension
thresholds are exceeded.  The package demonstrates how agents express their
philosophical views and evolve during a conversation.

## Installation

The project has no external dependencies and can be run directly after
cloning.  Optionally create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

No additional packages are required, so you can immediately run the examples
or tests.

## Running Tests

Unit tests are provided in the `tests/` directory.  Run them with:

```bash
pytest -q
```

This verifies state transitions and dialogue behaviour.

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")                # starts in Ego
agent2 = Agent("A2", state="Jaz")   # starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running the snippet shows how emotions trigger transitions from Ego to Jaz and
Jaz to Enotnost while the agents discuss absolute and relative truths.
