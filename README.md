# Divine-Ascension-System

A dynamic agent-based framework where ontological agents move through the
phases **Ego**, **Jaz**, and **Enotnost**. Emotional intensity and tension
drive these transitions while agents debate absolute, relative, and unified
truths.

## Running the Dialogue Simulation

Execute a short dialogue by launching Python and invoking
`philosophical_dialogue`:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")
for line in philosophical_dialogue(alice, bob):
    print(line)
PY
```

## Running Tests

Tests use `pytest`. Install the package if needed and run:

```bash
pytest -v
```

