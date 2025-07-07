# Divine-Ascension-System

This project simulates ontological agents engaged in philosophical debate. Agents transition through the states **Ego**, **Jaz**, and **Enotnost** based on their emotions and tension. The system demonstrates how emotional intensity influences philosophical viewpoints ranging from absolute to unified truths.

## Installation

Clone the repository and ensure you have Python 3.8 or later installed. Install dependencies using:

```bash
pip install -e .
```

## Running Tests

Execute the unit test suite with:

```bash
python -m pytest
```

## Example Usage

The example below runs `philosophical_dialogue` between two agents.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")            # defaults to Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this code prints a short conversation and shows each agent's state transitions.
