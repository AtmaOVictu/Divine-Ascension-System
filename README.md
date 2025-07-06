# Divine-Ascension-System

## Purpose

Divine-Ascension-System is a minimal framework for experimenting with agent-based philosophical interactions. Agents transition between ontological states (Ego, Jaz, Enotnost) based on their emotional intensity and tension. The project demonstrates how emotion-driven state changes influence philosophical dialogue.

## Installation

The package can be installed in editable mode so that local changes are immediately available:

```bash
pip install -e .
```

Alternatively, ensure the repository root is on your `PYTHONPATH` when running examples or tests.

## Example Usage

Below is a short example of creating two agents and running a philosophical dialogue between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script will show how the agents respond according to their ontological state and how they transition when emotions exceed their thresholds.

## Running the Tests

The test suite uses the standard `unittest` module. Run all tests with:

```bash
python -m unittest discover tests
```

This command will execute the unit tests in the `tests` directory and verify state transitions, responses, and dialogue generation.
