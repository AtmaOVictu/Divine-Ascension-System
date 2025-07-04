# Divine-Ascension-System

Divine-Ascension-System is a small experimental framework for modelling
ontological agents that evolve through three philosophical states:
**Ego**, **Jaz**, and **Enotnost**. An agent's current state depends on its
emotional intensity and tension level. When tension exceeds `0.7` or
emotion exceeds `0.5`, the agent advances from **Ego** to **Jaz** or
from **Jaz** to **Enotnost**.

Agents provide short philosophical responses based on their state and can
engage in dialogues that illustrate how emotions influence their
worldviews.

## Setup

1. Clone the repository and ensure you are using Python 3.11 or newer.
2. (Optional) Create and activate a virtual environment.
3. There are no extra dependencies – the repository works with the Python
   standard library.

## Running tests

Execute the test suite using `pytest`:

```bash
PYTHONPATH=. python -m pytest
```

All tests should pass and demonstrate correct state transitions and
responses.

## Example interaction

The snippet below runs a short dialogue between two agents and prints the
exchanged lines:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")          # starts at Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Typical output:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

This illustrates how emotional changes drive the agents toward more
unified philosophical perspectives.
