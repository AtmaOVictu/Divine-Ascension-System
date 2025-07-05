# Divine-Ascension-System

The Divine-Ascension-System is a lightweight Python framework that models
philosophical agents. Each agent can transition between three ontological states:
**Ego**, **Jaz**, and **Enotnost**. Emotions and tension influence these
transitions and shape the agents' responses about absolute, relative, and unified
truths. The system includes a simple dialogue simulation and unit tests
validating state changes and responses.

## Prerequisites

- Python 3.8 or newer
- No third-party packages are required.

## Running the Dialogue Demo

You can run a short philosophical dialogue in the shell:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1")                # starts in Ego
agent2 = Agent("Agent 2", state="Jaz")    # starts in Jaz
for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

This script creates two agents, triggers emotion changes, and prints their
conversation as they transition between states.

## Running Unit Tests

The project contains tests in the `tests` directory. Execute them with:

```bash
python -m unittest discover
```

This command runs the suite and verifies state transitions and dialogue output.
