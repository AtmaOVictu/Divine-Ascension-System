# Divine-Ascension-System

This project demonstrates a simple ontological agent framework. Agents move between three philosophical states while their emotions and tension guide the transitions. The states are implemented in [divine_agents/agent.py](divine_agents/agent.py) and a sample conversation is provided in [divine_agents/dialogue.py](divine_agents/dialogue.py).

## Ontological States

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships.
- **Enotnost** – All truths are one and interconnected.

## Installation

Clone the repository and install in editable mode:

```bash
pip install -e .
```

## Sample Dialogue

Run the following snippet to see a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Execute the unit tests with:

```bash
python -m unittest discover tests
```
