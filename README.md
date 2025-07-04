# Divine-Ascension-System

A minimal framework for experimenting with ontological agents. Agents move
between the philosophical states **Ego**, **Jaz**, and **Enotnost**. Emotional
intensity and tension drive these transitions and colour the agents' answers
about truth.

## Installation

The project has no third‑party dependencies. Clone the repository and use any
modern Python (3.8+).

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running the Tests

Execute the unit tests using the built-in `unittest` module:

```bash
python -m unittest discover -s tests
```

## Example Usage

Below is a short example showing how two agents engage in dialogue and
transition between states:

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
Agent1: S strastjo trdim: Resnica je relativna, oblikovana z našimi odnosi.
Agent2: S strastjo trdim: Vse resnice so eno, medsebojno povezane.
```

## Philosophical States

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by our relationships.
- **Enotnost**: All truths are one, interconnected.

## Development

To add new transitions or agent behaviour, extend the `Agent` class and the
`philosophical_dialogue` helper in `divine_agents/dialogue.py`. Unit tests in
`tests/` demonstrate expected behaviour and should be expanded alongside any new
features.
