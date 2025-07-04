# Divine-Ascension-System

This project models a small agent based simulation built around three
ontological states:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents store an emotional intensity and tension level. When tension is greater
than `0.7` or emotion greater than `0.5` the agent transitions from **Ego** to
**Jaz** or from **Jaz** to **Enotnost**. Dialogue between agents is influenced by
their emotional state, which is annotated in responses.

Unit tests (`tests/test_agents.py`) verify these transitions and responses.
