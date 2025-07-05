# AGENTS Guidelines

This repository contains a small framework for philosophical agents that
transition between three ontological states: **Ego**, **Jaz**, and
**Enotnost**. Agents update their internal *tension* and *emotion* values
and may change state when the following thresholds are reached:

- `tension` > `0.7` or `emotion` > `0.5`

The philosophical meaning of each state is:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

## Usage
1. Create one or more `Agent` instances from `divine_agents.agent`.
2. Interact with agents using the `respond()` method, which returns an
   answer appropriate for the agent's state.
3. Increase `emotion` or `tension` to trigger a state `transition()`.
4. Use `philosophical_dialogue()` from `divine_agents.dialogue` to
   generate a short exchange between two agents.

## Development notes
- Keep code modular and well documented.
- Add unit tests for new behaviours in the `tests/` folder.
- Run the test suite with `pytest -q` before committing changes.

These guidelines should help extend the system while preserving its
philosophical structure.
