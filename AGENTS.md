# AGENTS

This repository contains an ontological agent framework. Agents transition between
three philosophical states: **Ego**, **Jaz** and **Enotnost**. Transitions occur
when tension exceeds `0.7` or emotion intensity exceeds `0.5`. Emotions influence
responses and are stored together with a type such as `jeza` or `strah`.

## Files
- `divine_agents/agent.py` – agent class implementation.
- `divine_agents/dialogue.py` – functions for simulating philosophical dialogue.
- `tests/` – unit tests.

## Testing
Run tests with:
```bash
python -m pytest -q
```
