# Divine-Ascension-System

The Divine-Ascension-System simulates interactions between ontological agents.
Agents transition between philosophical states—**Ego**, **Jaz**, and **Enotnost**—
based on their emotions and tension. The project provides a small library for
experimenting with these transitions and generating dialogues that reflect each
agent's view of truth.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies (none are required beyond the Python standard library,
   but this step keeps the environment ready for future packages):
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is absent, you can skip this step.

## Running Tests

To run the unit tests use:
```bash
python -m unittest discover
```

## Usage Example

Run a simple dialogue between two agents:
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
This will print each line of the conversation, showing state transitions and
responses that reflect each agent's philosophy.
