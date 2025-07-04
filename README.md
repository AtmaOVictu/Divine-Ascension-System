# Divine-Ascension-System

This repository contains a minimal framework for simulating ontological agents.
Agents can transition between states (`Ego`, `Jaz`, `Enotnost`) based on their
current emotion and tension levels. The package also provides utilities for
generating short philosophical dialogues between agents.

## Modules
- `divine_agents.agent` – basic agent class handling state transitions.
- `divine_agents.dialogue` – helper for generating dialogues.
- `divine_agents.ouroboros` – an agent that cycles endlessly through the
  ontological states.

## Running tests
Install `pytest` and execute:

```bash
pytest -q
```

The tests verify state transitions, dialogue generation, and the cyclical
behaviour of the `OuroborosAgent`.
