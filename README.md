# Divine-Ascension-System

This repository contains a minimal agent-based framework that explores
transitions between three philosophical states:

- **Ego** – truth is absolute.
- **Jaz** – truth is relative.
- **Enotnost** – all truths are unified.

Agents update their state when their tension is greater than `0.7` or their
emotion exceeds `0.5`. The package provides a short dialogue example and unit
tests for these transitions.

## Quick start

Create a virtual environment with Python 3.11 and install `pytest` if not
already available.

Run the example dialogue:

```bash
python -m examples.agents_example
```

Execute the unit tests:

```bash
python -m pytest -q
```

The tests verify state transitions, agent responses and the sample dialogue.
