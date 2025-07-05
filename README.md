# Divine-Ascension-System

This project simulates agents that debate philosophy while transitioning between ontological states: **Ego**, **Jaz**, and **Enotnost**. Agents change state when their emotion or tension exceeds set thresholds and answer questions according to their current worldview.

## Installation

1. Create a virtual environment (optional but recommended).
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install the requirements.
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Execute the unit tests with:

```bash
python -m pytest -q
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents in different states
agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

# Engage in dialogue and print each line
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
