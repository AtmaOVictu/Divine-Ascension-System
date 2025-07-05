# Divine-Ascension-System

This repository provides a simple ontology-based agent framework. Agents
transition between **Ego**, **Jaz**, and **Enotnost** depending on their
emotional intensity and tension levels.

## Components
- **Agent** – encapsulates ontological state, tension, and emotion.
- **Generator** – acts as a catalyst that boosts an agent's emotion to
  trigger possible state transitions.
- **Dialogue** – utilities to simulate conversations between agents.

Run the unit tests with:

```bash
PYTHONPATH=. pytest -q
```
