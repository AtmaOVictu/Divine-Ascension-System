# Divine-Ascension-System

This project provides a minimal framework for simulating ontological agents. Agents can transition through three states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are interconnected.

State transitions occur when an agent's tension exceeds `0.7` or emotion exceeds `0.5`. A small dialogue helper demonstrates how agents can debate philosophical questions while updating their emotional state.

The module `interpolation.py` offers a utility for interpolating emotion and tension differences between two agents over a number of steps without external dependencies.

Run tests with:

```bash
PYTHONPATH=. pytest -q
```

