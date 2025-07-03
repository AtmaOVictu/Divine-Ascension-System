# Divine-Ascension-System

The Divine-Ascension-System simulates philosophical agents that transition
between the ontological states **Ego**, **Jaz**, and **Enotnost**. Each agent
holds an emotional state and a level of tension that can trigger these
transitions. The package provides simple tools to create agents and let them
engage in short dialogues about truth.

## Setup

1. Clone the repository.
2. Ensure you have Python 3 installed (no external dependencies are required).

```bash
python -m pip install --upgrade pip  # optional
```

## Example Usage

Create two agents and let them talk:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Agent 1 starts in Ego, Agent 2 in Jaz
agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script prints the philosophical conversation while showing state
transitions as emotions increase.

## Running Tests

Execute the test suite with `pytest`:

```bash
python -m pytest -q
```

All tests are located under the `tests/` directory and verify state transitions
and dialogue responses.
