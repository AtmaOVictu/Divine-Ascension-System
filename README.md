# Divine-Ascension-System

This project demonstrates a simple agent-based model where agents move
between ontological states **Ego**, **Jaz** and **Enotnost** based on their
emotions and tension. The system also includes a small dialogue engine
that shows how agents respond to philosophical questions depending on
their current state.

## Setup

The code requires Python 3.7+ and has no additional dependencies.
Clone the repository and run the tests to verify everything works:

```bash
python -m unittest discover -s tests
```

## Running a dialogue

The example below creates two agents and lets them discuss the nature
of truth. As their emotional state rises they transition to new states
and answer accordingly.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this snippet prints something similar to:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

The example shows both the initial responses and how the agents change
state once their emotion and tension pass the threshold.

## Running the tests

To validate the state transitions and dialogue logic run the unit tests
from the project root:

```bash
python -m unittest discover -s tests
```

The tests cover basic transitions and ensure that the dialogue returns
lines for each ontological state.
