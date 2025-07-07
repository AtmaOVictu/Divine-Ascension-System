# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

This repository contains a small ontological agent system. Agents can move from
`Ego` to `Jaz` and `Enotnost` depending on emotion and tension thresholds. Two
implementations are provided:

* `Agent` – a basic agent used in simple dialogues.
* `SelfAwareAgent` – extends the concept with reflection capabilities and
  records a history of transitions.

Unit tests located in `tests/` verify both transition logic and dialogue
behaviour.
