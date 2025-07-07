# Divine-Ascension-System

This project models dynamic philosophical agent interactions. Agents hold
ontological states—**Ego**, **Jaz**, or **Enotnost**—which represent differing
notions of truth. Their transitions are driven by emotional intensity and
tension.

## Setup Instructions

1. Install dependencies (none outside the standard library).
2. Run the unit tests:

```bash
pytest -q
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```
```
Alice (Ego): Resnica je absolutna in neodvisna od drugih.
Bob (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Alice prehaja v stanje: Jaz
Bob prehaja v stanje: Enotnost
Alice: Resnica je relativna, oblikovana z našimi odnosi.
Bob: Vse resnice so eno, medsebojno povezane.
```
