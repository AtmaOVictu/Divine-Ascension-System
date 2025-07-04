# Divine-Ascension-System

The Divine-Ascension-System is a simple Python framework for exploring
philosophical state transitions in an ontological setting. Agents move
between the states **Ego**, **Jaz**, and **Enotnost** based on their
emotions and tension levels. Dialogue examples and unit tests are
provided to demonstrate how the system behaves.

## Installation

The project only depends on Python 3.8 or newer and the standard
library. Clone the repository and, if desired, install the package in
editable mode:

```bash
pip install -e .
```

Alternatively you can simply set `PYTHONPATH` to the repository root
when running the examples or tests.

## Running the dialogue example

A small example is included in `divine_agents/dialogue.py`. After
cloning the repository, run:

```bash
PYTHONPATH=. python -m divine_agents.dialogue
```

This will execute a short conversation between two agents and display
how their states change in response to emotional updates.

## Running the tests

Unit tests are located in the `tests` directory. Execute them with:

```bash
PYTHONPATH=. python -m unittest -v tests/test_agents.py
```

All tests should pass and demonstrate correct state transitions and
responses.

