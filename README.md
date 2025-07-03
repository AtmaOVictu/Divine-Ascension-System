# Divine-Ascension-System

This project provides a minimal framework for simulating philosophical state transitions between ontological phases **Ego**, **Jaz**, and **Enotnost**. Agents update their tension and emotion levels which may trigger state transitions. Dialogues between agents showcase how their states influence their view on truth.

## Installation

Install the package in editable mode so tests can resolve imports:

```bash
pip install -e .
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

## Running Tests

After installation, run the unit tests with:

```bash
pytest
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
