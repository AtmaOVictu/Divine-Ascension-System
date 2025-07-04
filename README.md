# Divine-Ascension-System

A minimal framework for experimenting with ontological agents. Agents can
shift between the philosophical states **Ego**, **Jaz** and **Enotnost** while
engaging in dialogue. Transitions occur when an agent's tension rises above
`0.7` or its emotion level exceeds `0.5`.

## Installation

The project has no external dependencies. Clone the repository and ensure you
are using Python 3.8 or newer.

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running the Tests

Run the unit tests with `unittest`:

```bash
python -m unittest discover -s tests
```

## Example Usage

Below is a short example showing two agents engaging in dialogue and
transitioning between states.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent1")
agent2 = Agent("Agent2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Typical output is similar to:

```
Agent1 (Ego): Resnica je absolutna in neodvisna od drugih.
Agent2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Agent1 prehaja v stanje: Jaz
Agent2 prehaja v stanje: Enotnost
Agent1: Čutim jezo. Resnica je relativna, oblikovana z našimi odnosi.
Agent2: Čutim veselje. Vse resnice so eno, medsebojno povezane.
```

## Development

You can extend the system by adding new states or emotions. Pull requests are
welcome.

