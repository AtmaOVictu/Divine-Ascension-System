# Divine-Ascension-System

This project showcases a simple philosophical agent simulation. Agents move
between three ontological states:

* **Ego** – truth is absolute and independent.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents carry an emotional value and tension level. When emotion exceeds `0.5` or
tension rises above `0.7`, they transition to the next state. The included
`philosophical_dialogue` function demonstrates how two agents debate and evolve
through these states.

Run the unit tests to verify transitions and responses:

```bash
python -m pytest -q
```
