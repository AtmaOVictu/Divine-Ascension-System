# Divine-Ascension-System

This project demonstrates a simple agent based framework built around
three ontological states:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents transition between these states when their **tension** rises above
`0.7` or their **emotion** rises above `0.5`.  Transitions follow the
order `Ego → Jaz → Enotnost`.

The repository provides a minimal implementation of the agents and a
module that simulates a short philosophical dialogue between two agents.

## Installation

No external packages are required other than Python 3.  The test suite
can be executed either with the standard library `unittest` module or
with `pytest` for convenience.  To run the tests with `pytest` you may
install it via:

```bash
pip install pytest
```

## Running the tests

From the repository root run:

```bash
PYTHONPATH=. pytest
```

Alternatively you can execute:

```bash
python -m unittest discover
```

## Usage

The primary API consists of the `Agent` class and the `philosophical_dialogue`
function.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

conversation = philosophical_dialogue(a1, a2)
for line in conversation:
    print(line)
```

Each call to `philosophical_dialogue` will update the agents’ emotions,
trigger state transitions when thresholds are exceeded and produce lines
of dialogue reflecting their current states.
