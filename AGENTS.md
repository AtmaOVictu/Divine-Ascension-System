# Agent Framework

This project implements ontological agents that evolve through three philosophical states:

1. **Ego** – Truth is absolute and independent of others.
2. **Jaz** – Truth is relative, shaped by relationships and interactions.
3. **Enotnost** – All truths are unified and interconnected.

## State Transitions

Agents hold two primary values that influence their transitions:

- **Emotion** – intensity from 0.0 to 1.0.
- **Tension** – internal pressure from 0.0 to 1.0.

An agent attempts to transition when either `tension > 0.7` or `emotion > 0.5`.
The transition path is sequential:

- `Ego` → `Jaz` when thresholds are exceeded.
- `Jaz` → `Enotnost` when thresholds are exceeded again.

Each transition is recorded in the agent's history.

## Decision Logic

The `respond()` method provides philosophical answers based on the current state:

- **Ego** – returns an absolute view of truth.
- **Jaz** – returns a relative view of truth.
- **Enotnost** – returns a unified view of truth.

## Dialogue Simulation

The function `philosophical_dialogue()` in `divine_agents/dialogue.py` demonstrates a simple conversation and triggers state transitions by raising emotion levels.

## Testing

Unit tests in `tests/` verify transitions, responses, and sample dialogue. Run them with:

```bash
python -m unittest discover -s tests
```


