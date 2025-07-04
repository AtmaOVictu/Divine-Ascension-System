# Divine-Ascension-System

The **Divine-Ascension-System** provides a small agent framework for simulating
philosophical dialogues. Agents transition through the ontological states
**Ego**, **Jaz**, and **Enotnost** based on their emotional intensity and
internal tension. Each state influences how an agent perceives and describes
truth: absolute, relative, or unified.

## Installation

1. Install **Python 3.8** or later.
2. Clone this repository.
3. No additional packages are required.

```bash
python --version
```

## Running Tests

Execute the included unit tests with `unittest`:

```bash
python -m unittest discover -s tests
```

## Dialogue Example

Below is a short example of running the dialogue simulation in an
interactive Python session:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Which prints something similar to:

```text
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```
