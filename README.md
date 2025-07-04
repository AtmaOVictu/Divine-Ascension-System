# Divine-Ascension-System

The Divine-Ascension-System simulates philosophical agents that explore different ontological states. Each agent can transition between **Ego**, **Jaz**, and **Enotnost** based on emotion and tension levels. The project provides a small framework for building these agents and running dialogues between them.

## Main Modules

- **`divine_agents.agent`** – Defines the `Agent` class with state management, emotional/tension handling, and philosophical responses.
- **`divine_agents.dialogue`** – Contains helper functions for orchestrating conversations between agents.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Divine-Ascension-System
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install any required dependencies (none currently, but placeholder):
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Execute the unit tests using Python’s built-in unittest discovery:

```bash
python -m unittest discover -s tests
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This will create two agents and run a simple dialogue demonstrating state transitions and philosophical responses.
