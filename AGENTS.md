# Agent Design

This project implements ontological agents capable of moving through three
awareness states: **Ego**, **Jaz**, and **Enotnost**. Each agent tracks its
current state along with numeric values for **tension** and **emotion**.

## States
- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships.
- **Enotnost** – All truths are unified and interconnected.

## Transitions
Agents transition sequentially from *Ego* → *Jaz* → *Enotnost* when either of
these thresholds is exceeded:

- `tension > 0.7`
- `emotion > 0.5`

Whenever a transition occurs, the new state is recorded in the agent's history.

## Dialogue and Decisions
Agents respond to philosophical questions according to their current state. The
**dialogue** module demonstrates a simple interaction in which agents discuss the
nature of truth. Emotion updates during the conversation may cause further state
transitions.

## Testing
Unit tests live under the `tests/` directory and cover state transitions,
responses and dialogue behaviour. Run the suite with:

```bash
PYTHONPATH=. pytest -q
```
