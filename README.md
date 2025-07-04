# Divine-Ascension-System

## Agent System

This project implements a simple ontological agent model. Each `Agent` can be in one of three philosophical states: **Ego**, **Jaz**, or **Enotnost**. Agents hold a tension and emotion level that influence state transitions. When either the tension is greater than `0.7` or the emotion is above `0.5`, the agent may transition from Ego to Jaz or from Jaz to Enotnost. Agents respond to questions about truth according to their current state, reflecting absolute, relative, or unified perspectives.

## Installation

1. Clone the repository.
2. Ensure you have Python 3.8+ available.
3. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

## Running Tests

Execute the test suite using `unittest`:
```bash
python -m unittest discover -v -s tests
```

## Example Usage

Invoke a short philosophical dialogue between two agents:
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```
