# Divine-Ascension-System

Divine-Ascension-System is a minimal framework for experimenting with agent-based
dialogues. Agents transition between philosophical states—**Ego**, **Jaz**, and
**Enotnost**—based on their emotional intensity and tension. Each state reflects
a distinct notion of truth, from absolute to relative and finally unified. The
package includes simple utilities for simulating conversations and running unit
tests to verify agent behavior.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install the test dependency:
   ```bash
   pip install pytest
   ```

## Running the dialogue example

You can trigger a short conversation between two agents directly from the
interpreter:

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

This will print each line of the dialogue along with any state transitions.

## Running the tests

Run the unit tests with `pytest`. Ensure the project root is on the
`PYTHONPATH` so the package can be imported:

```bash
PYTHONPATH=. pytest
```

The tests confirm that state transitions occur when emotion or tension exceed
the defined thresholds and that the dialogue reflects the agents' states.

