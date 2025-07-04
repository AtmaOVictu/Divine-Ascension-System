# Divine-Ascension-System

Dynamic agent system exploring transitions between ontological states. Agents
move through **Ego**, **Jaz** and **Enotnost** based on their emotional intensity
and tension. Each state embodies a different view of truth:

* **Ego** – truth is absolute.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified.

The project provides utilities to simulate philosophical dialogue and observe
how agents react emotionally and philosophically as they shift states.

## Running a Sample Dialogue

`divine_agents/dialogue.py` contains a small example conversation. Execute it
with Python's module flag to see state transitions and responses:

```bash
python -m divine_agents.dialogue
```

## Running the Tests

Unit tests ensure state transitions occur at the correct thresholds and that
dialogue responses respect each agent's state. Run them with:

```bash
python -m pytest -q
```

## Requirements

The code targets **Python 3.11** and relies only on the Python standard
library. No additional dependencies are required.

