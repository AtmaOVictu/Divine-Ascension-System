# Divine-Ascension-System

This repository contains a small agent-based framework for simulating philosophical debates. Agents transition between ontological states (**Ego**, **Jaz**, and **Enotnost**) based on their emotions and tension levels. Unit tests verify that state transitions and philosophical responses behave as expected.

## Installation

1. **Python**: Ensure Python 3.8 or later is installed.
2. **Clone the repo**:
   ```bash
   git clone <repo-url>
   cd Divine-Ascension-System
   ```
3. **Install dependencies**: No external packages are required. (All modules use the Python standard library.)

## Running Tests

Execute the unit tests with the built-in test runner:

```bash
python -m unittest discover tests
```

## Example Usage

Create two agents and run a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Repository Structure

- `divine_agents/` – core modules (`agent.py`, `dialogue.py`)
- `tests/` – unit tests for agents and dialogues
- `TESTI.ipynb` – Jupyter notebook with experimental interactions
- `README.md` – project overview and usage instructions

