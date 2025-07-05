# Divine-Ascension-System

This project simulates philosophical dialogues between dynamic agents. Each agent can move between ontological states (**Ego**, **Jaz**, **Enotnost**) based on emotion and tension levels. As agents debate absolute, relative, and unified truths, their emotional responses drive state transitions, allowing you to explore how feelings influence philosophy.

## Installation

1. Clone this repository.
2. Create a Python environment (Python 3.11 or later recommended).
3. Install dependencies if any are added in the future (currently none are required).

## Running Tests

Set the `PYTHONPATH` to the repository root and execute `pytest`:

```bash
PYTHONPATH=. pytest -q
```

All tests should pass, verifying state transitions, responses, and dialogue behavior.

## Example Dialogue

You can initiate a short exchange using the provided `philosophical_dialogue` function:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this code will show how agents shift from **Ego** to **Jaz** or **Jaz** to **Enotnost** as their emotion levels rise, and how each state frames truth differently.
