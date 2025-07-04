# Divine-Ascension-System

A minimal agent-based framework exploring transitions between ontological states. Each agent can move from **Ego** to **Jaz** or from **Jaz** to **Enotnost** based on emotion and tension levels. Agents discuss absolute, relative, and unified truths according to their current state.

## Main Modules

- `divine_agents.agent` – defines the `Agent` class. Agents track their emotional intensity (`emotion`), tension, and ontological state. The `transition` method moves an agent to the next state when thresholds are exceeded, and `respond` generates a state-dependent philosophical answer.
- `divine_agents.dialogue` – provides `philosophical_dialogue` for simulating conversations between two agents, updating their emotions and triggering state transitions.

## Setup

This project requires Python 3. No additional third-party packages are needed aside from `pytest` for running the tests. Install it with:

```bash
pip install pytest
```

## Running Tests

Run the unit tests from the repository root using `pytest` with the repository in the `PYTHONPATH`:

```bash
PYTHONPATH=. pytest
```

Alternatively, if you package and install the project (for example with a `setup.py`), you can simply run `pytest` after installation.
