# Divine-Ascension-System

A minimal framework for simulating philosophical agents that transition
between ontological states based on emotion and tension.

## Installation

Clone the repository and ensure you have Python 3.8 or newer:

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

No external dependencies are required.

## Running Tests

Execute the unit tests using `unittest`:

```bash
python -m unittest discover -s tests
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

Typical output:

```
Agent1 (Ego): Resnica je absolutna in neodvisna od drugih. Čutim mirnost.
Agent2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi. Čutim mirnost.
Agent1 prehaja v stanje: Jaz
Agent2 prehaja v stanje: Enotnost
Agent1 (Jaz): Resnica je relativna, oblikovana z našimi odnosi. Čutim jezo.
Agent2 (Enotnost): Vse resnice so eno, medsebojno povezane. Čutim strah.
```

Agents shift from **Ego** to **Jaz** or **Enotnost** when their tension
exceeds `0.7` or emotion exceeds `0.5`. Responses always reflect the current
philosophical state and emotional tone.

