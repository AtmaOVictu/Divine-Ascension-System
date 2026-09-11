# Divine-Ascension-System

## Overview
The **Divine-Ascension-System** provides a minimal framework for simulating philosophical 
conversations. Each agent moves between three ontological states—**Ego**, **Jaz**, and
**Enotnost**—according to its emotional intensity and accumulated tension. These
transitions illustrate how perceptions of truth shift from absolute to relative and,
finally, to a unified perspective.

## Environment Setup
1. Install Python 3.8 or later.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install test dependencies:
   ```bash
   pip install pytest
   ```
   No additional packages are required for the core library.

## Running the Tests
Run the unit tests with `pytest` from the project root:
```bash
pytest
```

## Example Usage
A short demonstration of two agents debating truth:
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")          # starts in Ego
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
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
