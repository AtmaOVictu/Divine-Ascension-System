# Divine-Ascension-System

This project contains simple ontological agents that transition between states
(Ego, Jaz, Enotnost) based on tension and emotion levels.

## Modules
- `agent.py` defines the base `Agent` with state transitions and responses.
- `dialogue.py` simulates a short philosophical dialogue between two agents.
- `extensions.py` introduces additional components:
  - `Samoregulacija` for energy self-regulation.
  - `VecDimenzionalniAgent` representing agents that move through dimensions.
  - `Ucenje` for storing experiences.
  - `CustvenaDinamika` to manage emotional states.

## Tests
Run tests with:
```bash
PYTHONPATH=. pytest -q
```

