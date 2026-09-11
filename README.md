# Divine-Ascension-System

This project models philosophical agents transitioning between ontological
states: **Ego**, **Jaz**, and **Enotnost**. Agents interact through dialogues
where emotions and tension influence their philosophical stance.

## Setup

The project requires Python 3.11+. Install the dependencies and run the tests:

```bash
pip install -r requirements.txt  # if a requirements file exists
python -m pytest -q
```

## Usage

You can create agents and simulate a dialogue:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
lines = philosophical_dialogue(a1, a2, exchanges=2)
for line in lines:
    print(line)
```

## Tests

Run all unit tests with:

```bash
python -m pytest -q
```
