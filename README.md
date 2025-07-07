# Divine-Ascension-System

This project implements a simple ontological agent framework. Agents progress through
three philosophical states—**Ego**, **Jaz**, and **Enotnost**—based on their emotions
and tension levels. The system is intended to explore interactions and dialogues
where different perceptions of truth evolve over time.

## Philosophical States

- **Ego**: Truth is **absolute** and independent of others.
- **Jaz**: Truth is **relative** and shaped by relationships.
- **Enotnost**: All truths are **unified** and interconnected.

An agent transitions from *Ego* to *Jaz*, or from *Jaz* to *Enotnost*, when its
tension exceeds `0.7` or its emotion rises above `0.5`.

## Running the Dialogue Demo

You can run a sample dialogue between two agents from the command line:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

This script will display how each agent transitions and responds according to
their current philosophical state.

## Running Unit Tests

Execute all tests with Python's built-in `unittest` module:

```bash
python -m unittest
```

## Python Compatibility and Dependencies

The codebase requires **Python 3.8** or newer and has no external dependencies.
Only the standard library is used.
