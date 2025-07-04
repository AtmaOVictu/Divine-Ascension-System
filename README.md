# Divine-Ascension-System

A minimal framework for experimenting with ontological agents. Agents can shift
between the philosophical states **Ego**, **Jaz** and **Enotnost** and respond to
questions according to their current state.

## Installation

The project relies only on the Python standard library. Clone the repository and
use any modern Python (3.8+).

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running the Tests

Execute the unit tests using `unittest`:

```bash
python -m unittest discover -s tests
```

## Example Usage

Below is a short example showing how two agents engage in dialogue and transition
between states:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent1")
agent2 = Agent("Agent2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script prints output similar to:

```
Agent1 (Ego): Resnica je absolutna in neodvisna od drugih.
Agent2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Agent1 prehaja v stanje: Jaz
Agent2 prehaja v stanje: Enotnost
Agent1: Resnica je relativna, oblikovana z našimi odnosi.
Agent2: Vse resnice so eno, medsebojno povezane.
```
