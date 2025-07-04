# Divine-Ascension-System

`Divine-Ascension-System` is a small demonstration of agents that discuss
philosophy while their emotional state drives transitions between three
ontological phases:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents adjust their tension and emotion levels during a conversation. When the
levels pass certain thresholds, a state transition occurs and the agent's view
of truth changes.

## Usage

The package exposes an `Agent` class and a `philosophical_dialogue` helper in
`divine_agents`.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")  # starts in Ego
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

The snippet above prints a short debate between two agents and shows any state
changes triggered by their emotions.

## Running tests

Unit tests live under the `tests` directory. Ensure the repository root is on
the Python path and run `pytest`:

```bash
PYTHONPATH=. pytest
```

The test suite verifies state transitions, responses, and dialogue behaviour.
