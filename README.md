# Divine-Ascension-System

`divine_agents` is a minimal library demonstrating philosophical agents who change ontological states based on emotion and tension. The agents discuss truth from different perspectives: **Ego**, **Jaz**, and **Enotnost**.

## Installation

This project has no external dependencies. Clone the repository and install the package in editable mode:

```bash
pip install -e .
```

## Running Tests

Execute the unit tests using the standard library's test runner:

```bash
python -m unittest discover -s tests
```

## Example Dialogue

The library includes a helper to simulate a short conversation between two agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```


