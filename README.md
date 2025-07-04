# Divine-Ascension-System

This project demonstrates a simple framework for simulating ontological agents. Each agent can be in one of three philosophical states:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are one and interconnected.

Agents adjust their emotional intensity and tension during interaction. When tension exceeds `0.7` or emotion exceeds `0.5`, agents transition from **Ego** → **Jaz** → **Enotnost**. Dialogue functions provide examples of how these agents debate absolute and relative truths while their emotions cause state changes.

## Requirements

- **Python**: 3.11 or later
- **Dependencies**: none besides the standard library. `pytest` is needed only for running the tests.

## Running an Example Dialogue

To observe a short philosophical debate, execute the following from the project root:

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

This script instantiates two agents and prints the conversation as they transition between states.

## Running Tests

Unit tests verify state transitions, philosophical responses, and dialogue flow. Execute them using `pytest` with the project root on the `PYTHONPATH`:

```bash
PYTHONPATH=. pytest -q
```

All tests should pass, indicating that transitions occur once the tension or emotion thresholds are met and that dialogue lines reflect the agents' states.

