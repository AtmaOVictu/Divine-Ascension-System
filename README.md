# Divine-Ascension-System

This project implements a minimal agent-based system demonstrating
philosophical state transitions. Agents move from **Ego** to **Jaz** and
finally **Enotnost** as their tension and emotion increase.

## Usage

The package can be used directly without installation by running the
`dialogue.py` script or importing the `Agent` class.

```
python -m divine_agents.dialogue
```

## Running Tests

Install `pytest` and run the unit tests from the project root:

```
pip install pytest
pytest -q
```

The tests verify state transitions, responses, and a short dialogue between
agents.
