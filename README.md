# Divine-Ascension-System

This project models ontological agents that transition between philosophical
states based on their emotions and tension. Agents begin in **Ego**, may move to
**Jaz**, and ultimately reach **Enotnost**. State transitions occur when the
agent's tension exceeds `0.7` or emotion exceeds `0.5`.

## Setup Instructions

1. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt  # optional
   ```
2. Run the test suite:
   ```bash
   pytest
   ```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Example output:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```
