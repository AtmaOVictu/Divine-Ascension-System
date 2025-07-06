# Divine-Ascension-System

This project simulates agents that shift through philosophical states—**Ego**, **Jaz**, and **Enotnost**—according to their emotional intensity and tension levels. Each state reflects a different view of truth:

- **Ego**: truth is absolute and independent of others.
- **Jaz**: truth is relative and shaped by relationships.
- **Enotnost**: all truths are unified and interconnected.

Agents engage in short dialogues where their responses depend on both their ontological state and their current emotions.

## Installation

This project has no external dependencies beyond Python 3. To run the examples or tests, ensure that Python 3.8+ is installed.

```bash
python -m pip install -r requirements.txt  # if a requirements file is provided
```

## Usage

To run a simple dialogue between two agents:

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Unit Tests

Execute the tests with:

```bash
python -m unittest discover
```

Contributions are welcome via pull requests.
