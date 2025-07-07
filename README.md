# Divine-Ascension-System
A small framework for simulating philosophical agents that evolve through ontological states. Agents transition from **Ego** to **Jaz** or **Enotnost** based on their emotion and tension levels and engage in dialogues about absolute and relative truths.

## Installation
This project requires Python 3. There are no external dependencies, but you can install optional packages with:

```bash
pip install -r requirements.txt
```

## Running Tests
Execute the unit tests using:

```bash
python -m unittest tests/test_agents.py
```

## Example Usage
The snippet below instantiates two agents and runs a short dialogue between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
