# Divine-Ascension-System

The **Divine Ascension System** provides a simple framework for simulating ontological agents that transition between philosophical states (Ego, Jaz, Enotnost). Agents adjust their state based on emotional intensity and tension and can engage in short philosophical dialogues about the nature of truth.

## Installation

The project has no external dependencies beyond Python 3. To work with the code locally, clone the repository and optionally create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -U pip
```

No additional packages are required.

## Running a Dialogue

The `divine_agents` package exposes the `Agent` class and a convenience function `philosophical_dialogue` for running a short conversation between two agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents with different starting states
agent1 = Agent("A1")            # defaults to state "Ego"
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script will display each agent's view of truth and demonstrate how their states change when emotion increases.

## Running Tests

Unit tests validate agent behaviour and dialogue generation. Use `pytest` with the repository root on the `PYTHONPATH`:

```bash
PYTHONPATH=. pytest
```

Alternatively you can run the tests directly with Python's unittest module:

```bash
PYTHONPATH=. python -m tests.test_agents
```

The tests ensure that state transitions occur when tension or emotion cross the required thresholds and that dialogue lines reference the correct ontological states.

