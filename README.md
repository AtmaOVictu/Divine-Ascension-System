# Divine-Ascension-System

This project demonstrates a simple ontological framework where agents move
between the states **Ego**, **Jaz** and **Enotnost**. Transitions depend on each
agent's emotional intensity and tension.

## Structure

- `divine_agents` – package containing the agent implementation and tools for
  generating philosophical dialogues.
- `tests` – unit tests covering state transitions and dialogues.

## Usage

1. Install dependencies (only `pytest` is required for tests).
2. Run the example simulation:

```bash
python -m divine_agents.dialogue
```

3. Execute the unit tests:

```bash
pytest
```

## Philosophy

An agent in **Ego** believes truth is absolute. In **Jaz**, truth becomes
relative, while **Enotnost** represents the unified perspective where all truths
are connected. Emotional states influence tension, which in turn drives the
transition through these stages.
