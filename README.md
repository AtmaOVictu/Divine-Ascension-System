# Divine-Ascension-System

This project demonstrates a minimal agent-based framework focused on
philosophical state transitions. Agents move between three ontological
states – **Ego**, **Jaz**, and **Enotnost** – depending on their emotion
and tension levels.  Thresholds for transitions are defined as tension
greater than `0.7` or emotion greater than `0.5`.

The package exposes simple utilities to create agents and run dialogues
between them.  Agents can also belong to broad philosophical groups such
as `Dualistic` or `Relational`, which helps organise larger simulations.

## Running Tests

Install `pytest` and run:

```bash
pytest
```
