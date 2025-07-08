# Divine-Ascension-System

This project simulates interactions between ontological agents that progress through philosophical states. The main goal is to model how emotions and tension drive agents from **Ego** through **Jaz** to **Enotnost** and how these states influence their dialogue about truth.

## Modules

- **divine_agents/agent.py** – Defines the `Agent` class. Each agent holds its current state, emotion, and tension and can transition to a new state when thresholds are exceeded. The `respond` method returns a statement about truth based on the agent's state.
- **divine_agents/dialogue.py** – Contains the `philosophical_dialogue` function, which orchestrates a brief conversation between two agents. It updates their emotions, triggers state transitions, and gathers their responses.

## Setup

1. Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install the required dependencies (for this project there are none outside the standard library, but `pip` can be used for future packages):
   ```bash
   pip install -r requirements.txt  # if such a file is added later
   ```

## Running Tests

Unit tests are located in the `tests/` directory. To run them execute:

```bash
python -m unittest discover -s tests
```

## Example Usage

Below is a quick example showing how to create agents and run a dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")                 # Starts in Ego
agent2 = Agent("A2", state="Jaz")     # Starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this code will print a small conversation, demonstrating how each agent's state and emotions affect their view on truth and how they transition between states.
