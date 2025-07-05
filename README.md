# Divine-Ascension-System

This project demonstrates a simple ontological framework where agents move
between three philosophical states:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships.
- **Enotnost** – All truths are unified and interconnected.

Agents hold `emotion` and `tension` values. When either the tension exceeds
`0.7` or emotion exceeds `0.5`, the agent transitions to the next state in the
sequence (Ego → Jaz → Enotnost). Responses given by an agent depend on its
current state.

The package also provides a `MultiAgentSystem` for updating several agents at
once and a `ReflectiveAgent` that can perform a basic form of self-reflection
based on its history.

Unit tests cover state transitions, responses, dialogues, and the additional
classes.
