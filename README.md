# Divine-Ascension-System

A minimal framework for experimenting with ontological agents. Each agent
maintains an emotional state and level of tension. When tension exceeds `0.7`
or emotion intensity exceeds `0.5`, agents transition through the philosophical
states **Ego**, **Jaz** and **Enotnost**.

## Installation

The project relies only on the Python standard library. Clone the repository and
use a modern Python (3.8+).

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running the Tests

Execute the unit tests using `pytest` (included in the standard library via
`unittest`).

```bash
python -m pytest -q
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent1")
agent2 = Agent("Agent2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this snippet prints output similar to:

```
Agent1 (Ego): Resnica je absolutna in neodvisna od drugih.
Agent2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Agent1 prehaja v stanje: Jaz
Agent2 prehaja v stanje: Enotnost
Agent1: Resnica je relativna, oblikovana z našimi odnosi. Počutim se jezno.
Agent2: Vse resnice so eno, medsebojno povezane. Počutim se radostno.
```

This demonstrates how emotional intensity triggers transitions and influences
responses.
