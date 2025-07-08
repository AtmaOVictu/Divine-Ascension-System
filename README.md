# Divine-Ascension-System

This repository contains a small agent framework called `divine_agents`. The
library demonstrates how agents can move between ontological states based on
tension and emotion while debating different notions of truth.

## Purpose of `divine_agents`

`divine_agents` provides two main modules:

* **`agent`** – defines the `Agent` class with states **Ego**, **Jaz** and
  **Enotnost**. Agents adjust emotion and tension, transition between states
  when thresholds are exceeded and respond to questions about truth from their
  current philosophical viewpoint.
* **`dialogue`** – contains helper functions for simulating a short
  conversation between two agents, showing how emotions can trigger state
  changes during a debate.

These components are meant for educational use and can be extended for more
complex simulations.

## Running a demonstration

A minimal demonstration is provided via the `philosophical_dialogue` function.
Execute the following snippet to see two agents interact:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
PY
```

This prints a brief conversation and displays state transitions triggered by
rising emotions.

## Running unit tests

Unit tests live in the `tests` directory. Run them with:

```bash
python -m unittest discover -s tests
```

## Installation

The project can be used directly from the repository. If you introduce a
packaging step (for example by creating a `pyproject.toml` or `setup.cfg`), you
may install it in editable mode with:

```bash
pip install -e .
```

