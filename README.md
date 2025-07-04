# Divine-Ascension-System

This project provides a simple agent-based framework exploring three ontological states:
**Ego**, **Jaz**, and **Enotnost**. Agents adjust their emotion and tension levels
and transition between states when the defined thresholds are met. The
`divine_agents` package also contains a dialogue module that demonstrates
philosophical conversations about absolute, relative and unified truths.

## Installation

1. Clone this repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the only dependency used for testing:

   ```bash
   pip install pytest
   ```

## Usage

- `divine_agents/agent.py` defines the `Agent` class and its state transition logic.
- `divine_agents/dialogue.py` contains a helper for running a short dialogue
  between two agents.

You can experiment with the system in a Python shell:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent1")
agent2 = Agent("Agent2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

To execute the unit tests run:

```bash
python -m pytest
```

This command discovers and runs tests in the `tests` directory.
