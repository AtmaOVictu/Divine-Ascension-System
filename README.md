# Divine-Ascension-System

This project simulates philosophical agents that evolve through ontological states. Each agent can transition between **Ego**, **Jaz**, and **Enotnost** based on emotion and tension levels. The dialogue system demonstrates how agents debate absolute, relative, and unified truths while their emotions influence the discussion.

## Ontological framework

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative, shaped by relationships.
- **Enotnost**: All truths are one and interconnected.

Agents transition from one state to the next when their **tension** exceeds `0.7` or their **emotion** exceeds `0.5`.

The core modules are:

- `divine_agents.agent` – defines the `Agent` dataclass and state-transition logic.
- `divine_agents.dialogue` – provides `philosophical_dialogue` to run a sample conversation.
- `divine_agents.initialize_agents` – quickly creates two default agents for experimentation.

## Installation

The library has no external runtime dependencies. To run the tests you will need `pytest`:

```bash
pip install pytest
```

## Running a sample dialogue

Execute the following command to see two agents debate truth:

```bash
python - <<'PY'
from divine_agents import initialize_agents, philosophical_dialogue

agent1, agent2 = initialize_agents()
for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

## Running the unit tests

Run the tests using `pytest`:

```bash
python -m pytest -q
```

The tests verify state transitions, agent responses, and dialogue generation.
