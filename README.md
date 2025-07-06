# Divine-Ascension-System

This project models conversations between ontological agents transitioning through
three philosophical states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative, shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents hold an emotion level and a tension level. When **tension** exceeds `0.7`
or **emotion** exceeds `0.5`, an agent moves from `Ego` to `Jaz` or from `Jaz` to
`Enotnost`. These transitions and the responses for each state are implemented in
`divine_agents/agent.py`.

The function `philosophical_dialogue` in `divine_agents/dialogue.py` demonstrates
how two agents interact and evolve as their emotions rise.

## Requirements
The system has no external dependencies beyond Python (version 3.8 or newer is
recommended). Optionally create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

## Running Tests
All tests reside in the `tests` directory. Execute them with:

```bash
python -m unittest
```

This command will automatically discover and run the unit tests verifying state
transitions and dialogue behaviour.
