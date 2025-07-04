# Divine-Ascension-System

The Divine Ascension System is a small agent-based simulation built around an ontological framework. Agents move through three philosophical states based on their emotion and tension levels:

- **Ego (⊘)** – truth is absolute and independent of others.
- **Jaz (∫(dru/x))** – truth is relative and shaped by our relationships.
- **Enotnost (RES001)** – all truths are one and interconnected.

Agents transition from Ego to Jaz or Jaz to Enotnost when their tension exceeds `0.7` or their emotion exceeds `0.5`. Dialogues show how each state influences the view of truth.

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# create two agents in different states
agent1 = Agent("Agent 1")          # starts in Ego
agent2 = Agent("Agent 2", state="Jaz")

# run a simple dialogue
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running the Tests

The repository includes unit tests under `tests/`. Ensure the repository root is on the Python path and run:

```bash
PYTHONPATH=. pytest
```

All tests should pass and verify state transitions, responses, and dialogue generation.

## Contact

For questions or contributions, please open an issue on the repository or contact `maintainer@example.com`.
