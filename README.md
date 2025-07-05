# Divine-Ascension-System

This project simulates a set of philosophical agents that can transition
through the ontological states **Ego**, **Jaz** and **Enotnost**.  Transitions
are triggered once an agent's tension rises above `0.7` or its emotion
intensity exceeds `0.5`.

The package contains a simple dialogue engine where agents debate absolute,
relative and unified truths.  Agents react emotionally which in turn affects
their tension and causes state changes.

## Running the tests

Execute the unit tests with `pytest` and the project root on `PYTHONPATH`::

    PYTHONPATH=. pytest -q

