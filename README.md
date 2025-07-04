# Divine-Ascension-System

This repository provides a small ontological agent framework. Each agent can exist in one of three philosophical states:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by our relationships.
- **Enotnost** – Truth is unified and interconnected.

Agents carry `tension` and `emotion` values. When `tension` exceeds `0.7` or `emotion` exceeds `0.5`, the agent transitions to the next state (Ego → Jaz → Enotnost). A helper function is provided to simulate a philosophical dialogue demonstrating these transitions.

## Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("Filozof1")            # starts in Ego
a2 = Agent("Filozof2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

Running the snippet prints lines similar to:

```
Filozof1 (Ego): Resnica je absolutna in neodvisna od drugih.
Filozof2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Filozof1 prehaja v stanje: Jaz
Filozof2 prehaja v stanje: Enotnost
Filozof1: Resnica je relativna, oblikovana z našimi odnosi.
Filozof2: Vse resnice so eno, medsebojno povezane.
```

## Running the tests

The unit tests validate state transitions and dialogue output. Execute them with:

```
python3 -m pytest
```

After installing the package in editable mode (`pip install -e .`), you may simply run:

```
pytest
```
