# Divine-Ascension-System

This project demonstrates ontological agents that evolve through states based on
emotion and tension. The code is pure Python and has no third-party
requirements.

## Installation

1. Ensure Python 3.8+ is installed.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies (there are none, but install `pytest` if you prefer it
   for running tests):
   ```bash
   pip install -U pytest
   ```

## Running Tests

Execute the unit tests with the built-in `unittest` runner:

```bash
python -m unittest discover -s tests
```

If you installed `pytest`, you can instead run:

```bash
pytest
```

## Using the Library

### Agent

```python
from divine_agents.agent import Agent

agent = Agent("Ana")
agent.update_emotion(0.6)  # increases emotion and tension
new_state = agent.transition()  # state may shift if thresholds are exceeded
print(new_state)
```

### philosophical_dialogue

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")
for line in philosophical_dialogue(alice, bob):
    print(line)
```

## State Transition Thresholds

Agents move from **Ego** to **Jaz** or **Jaz** to **Enotnost** when either:

- **Emotion** exceeds **0.5**, or
- **Tension** exceeds **0.7**.

These thresholds determine whether the `transition` method updates the agent's
state. The states embody philosophical views:

- **Ego** – truth is absolute.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are one and interconnected.
