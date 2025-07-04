# Divine Ascension System

This project demonstrates a simple agent-based model built around an
ontological framework. Agents evolve through three philosophical states:
**Ego**, **Jaz**, and **Enotnost**. Transitions are triggered when an
agent's tension exceeds `0.7` or its emotional intensity surpasses
`0.5`.

## Usage

### Running the dialogue simulation

```bash
python -m divine_agents.dialogue
```

### Running tests

```bash
python -m pytest -q
```

## Project structure

- `divine_agents/agent.py` – Agent implementation with state management.
- `divine_agents/dialogue.py` – Utilities for simulating philosophical
  dialogues.
- `tests/` – Unit tests covering transitions and responses.

The system showcases how emotional intensity influences philosophical
responses and drives transitions between ontological states.
