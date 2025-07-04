# Divine-Ascension-System

This project implements a minimal agent framework used to explore ontological
states and philosophical dialogues. Agents transition between **Ego**, **Jaz**,
and **Enotnost** depending on their emotional intensity and tension.

## Installation

It is recommended to install the package in editable mode so that the tests and
examples can import the `divine_agents` package directly:

```bash
pip install -e .
```

## Basic Usage

Create agents and run a philosophical dialogue between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")           # defaults to the Ego state
agent2 = Agent("A2", state="Jaz")

# engage in conversation and allow emotions to trigger transitions
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Example output will show how each agent answers from its current state and when
the state changes (e.g. Ego → Jaz or Jaz → Enotnost) once the emotion or
tension thresholds are reached.

You can also manually manipulate an agent's emotion to trigger a transition:

```python
agent = Agent("Solo")
print(agent.state)  # Ego
agent.update_emotion(0.6)
print(agent.transition())  # Jaz
```

## Running Tests

Tests are provided with `pytest` and ensure that state transitions and dialogue
responses behave as expected. After installing the package, run:

```bash
python -m pytest
```

This will execute the unit tests in the `tests/` directory.
