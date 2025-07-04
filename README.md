# Divine-Ascension-System

Divine-Ascension-System is a small experimental framework for simulating agents that shift between philosophical states. Agents begin in **Ego**, may move to **Jaz**, and finally to **Enotnost** when their emotional intensity or tension surpasses certain thresholds.

Each ontological state guides how an agent perceives truth:

* **Ego** – Truth is absolute and independent of others.
* **Jaz** – Truth is relative and shaped by relationships.
* **Enotnost** – All truths are interconnected as one.

Agents update their emotional level and tension as they converse. When `tension > 0.7` or `emotion > 0.5`, a state transition is triggered.

## Basic Usage

The package provides an `Agent` class and a helper `philosophical_dialogue` function. The snippet below demonstrates simple usage:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

Running this script prints a short conversation and shows the agents transitioning between states as their emotions rise.

## Running the philosophical dialogue demo

There is no separate executable. Launch a Python interpreter and execute the example above (or place it in a script). Ensure the repository root is on `PYTHONPATH` so the `divine_agents` package can be imported:

```bash
PYTHONPATH=. python demo.py
```

where `demo.py` contains the snippet under **Basic Usage**.

## Running the tests

Unit tests live in the `tests/` directory. Execute them using `pytest`:

```bash
PYTHONPATH=. python -m pytest -q
```

All tests should pass, verifying state transitions, responses, and the dialogue logic.

