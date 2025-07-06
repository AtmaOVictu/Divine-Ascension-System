# Divine-Ascension-System

This project demonstrates a minimal ontological agent model. Agents can be in
three philosophical states:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are one and interconnected.

Agents transition between states when their tension exceeds `0.7` or their
emotional intensity rises above `0.5`. Emotions influence how an agent responds
in dialogue and directly affect their tension.

The module `divine_agents.dialogue` contains a small simulation where two agents
discuss truth and evolve through states. Unit tests in `tests/` verify
transitions, emotional responses and the generated dialogue.
