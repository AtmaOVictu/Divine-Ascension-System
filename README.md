# Divine-Ascension-System

Divine Ascension System simulates ontological agents that evolve through three philosophical states:

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are one, interconnected.

Agents hold a level of **tension** and **emotion**. When tension exceeds `0.7` or emotion exceeds `0.5`, an agent transitions from `Ego` to `Jaz` or from `Jaz` to `Enotnost`. Their responses change according to the current state.

The repository provides a simple dialogue simulation where two agents discuss the nature of truth and change state based on emotional intensity.

## Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd Divine-Ascension-System
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. No external dependencies are required. Ensure you have Python 3.8+ installed.

## Running the Dialogue Example

Execute the following Python snippet to see a sample conversation:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent('A1')
agent2 = Agent('A2', state='Jaz')

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

## Running Tests

Use `pytest` via the Python module flag so that the local package is discovered:

```bash
python -m pytest -q
```

All tests should pass and confirm that state transitions and dialogue behaviour work as expected.

