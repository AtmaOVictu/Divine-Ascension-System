# Divine-Ascension-System

The Divine Ascension System simulates agents that move through three
ontological states &mdash; **Ego**, **Jaz**, and **Enotnost** &mdash; depending on
their emotional intensity and tension. Agents debate philosophical
principles such as absolute, relative, and unified truth.

## Setup

1. Clone this repository.
2. Ensure Python 3.8 or newer is available.
3. (Optional) Create a virtual environment and activate it.
4. There are no additional dependencies required.

## Running Tests

Execute the unit tests with:

```bash
python -m pytest
```

This command ensures the package path is correctly resolved and runs all
checks found in the `tests/` directory.

## Example Usage

The following snippet demonstrates a short dialogue and the resulting
state transitions:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")                # Starts in Ego
agent2 = Agent("A2", state="Jaz")    # Starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this code will produce output similar to:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

This demonstrates how rising emotion triggers transitions from Ego to Jaz
and from Jaz to Enotnost while the agents debate truth.
