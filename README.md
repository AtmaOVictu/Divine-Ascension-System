# Divine-Ascension-System

The Divine Ascension System is a small simulation of ontological agents that evolve through three philosophical states: **Ego**, **Jaz**, and **Enotnost**. Each agent tracks its emotional intensity and tension level. When either the tension exceeds 0.7 or the emotion exceeds 0.5, the agent transitions to the next state.

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

## Running the dialogue demo

A simple demonstration script is included to show two agents debating truth and transitioning between states:

```bash
python demo.py
```

This will print a short conversation where each agent responds according to its current ontological state, updates emotion, and possibly changes state.

## Running the tests

Unit tests are provided in the `tests` directory. Execute them with:

```bash
python -m pytest -q
```

The tests verify correct state transitions, philosophical responses, and that a dialogue produces an `Enotnost` state.

