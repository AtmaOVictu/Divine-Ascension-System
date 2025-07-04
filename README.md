# Divine-Ascension-System

The Divine-Ascension-System simulates agents that progress through ontological states while engaging in philosophical debate. Each agent maintains an emotional and tension level which drives transitions between the states **Ego**, **Jaz**, and **Enotnost**.

## Installation

Create a virtual environment and install any optional development tools. The project itself has no mandatory third‑party dependencies.

```bash
python -m venv venv
source venv/bin/activate
pip install -U pip
```

If you want to run the test suite with `pytest`, install it as well:

```bash
pip install pytest
```

## Running the Dialogue Example

You can run the short built-in dialogue directly with Python:

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

This will print a conversation where both agents potentially change states based on their updated emotions.

## Running Tests

The project uses the standard `unittest` framework. Run all tests with:

```bash
python -m unittest discover
```

If you installed `pytest`, you can alternatively execute:

```bash
pytest
```

## Agent States and Transitions

Agents begin in one of three ontological states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and formed through relationships.
- **Enotnost** – all truths are unified and interconnected.

An agent transitions from **Ego** to **Jaz**, or from **Jaz** to **Enotnost**, when its `tension` exceeds `0.7` or its `emotion` exceeds `0.5`. These thresholds are evaluated whenever `Agent.transition()` is called.

