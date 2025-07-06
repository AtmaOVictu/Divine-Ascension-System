# Divine-Ascension-System

This project contains a small ontological simulation of agents that
transition through the states **Ego**, **Jaz** and **Enotnost**.  Agents
change their state when their internal tension exceeds ``0.7`` or when
their emotional intensity goes beyond ``0.5``.

The package exposes two simple modules:

* ``agent`` – represents an individual agent with tension and emotion.
* ``dialogue`` – orchestrates a short philosophical discussion between
  two agents.

Unit tests can be executed with ``pytest``.
