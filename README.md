# Divine-Ascension-System

This project demonstrates a simple ontological agent system. Agents hold an
ontological state (``Ego``, ``Jaz`` or ``Enotnost``) and can transition between
states when their **tension** or **emotion** exceeds a threshold. Each state
reflects a different philosophical principle of truth:

* **Ego** – Truth is absolute and independent of others.
* **Jaz** – Truth is relative and shaped by relationships.
* **Enotnost** – All truths are one and interconnected.

Agents update their emotional state through ``update_emotion`` which also
increases tension. When tension ``> 0.7`` or emotion ``> 0.5`` they transition to
the next state via ``transition``.

The module ``divine_agents.dialogue`` provides a helper to simulate a short
dialogue demonstrating these transitions.

Run the unit tests with::

    python -m unittest

to validate the behaviour of the system.
