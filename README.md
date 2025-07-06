# Divine-Ascension-System

This project provides a simple framework for experimenting with ontological
agents that transition between the states **Ego**, **Jaz**, and **Enotnost**.
The core logic is implemented in `divine_agents` and includes utilities for
running short philosophical dialogues.

## Usage

Agents react to changes in `tension` and `emotion`. When `tension` exceeds
`0.7` or `emotion` exceeds `0.5`, an agent transitions to the next state.
Responses depend on the current state:

- **Ego** – truth is absolute.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified.

### Graphical Interface

A minimal Tkinter application is provided in `divine_agents/gui.py`.
Run it with:

```bash
python -m divine_agents.gui
```

The interface visualizes the agent as a coloured circle and offers buttons to
increase tension or emotion to trigger state transitions in real time.

## Running Tests

Execute the unit tests using `pytest` via the Python module syntax:

```bash
python -m pytest -q
```
