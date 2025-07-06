# Divine-Ascension-System

Divine-Ascension-System is a small demonstration of a dynamic agent-based framework. Each agent can move through philosophical states—**Ego**, **Jaz**, and **Enotnost**—depending on its emotional intensity and tension. These transitions shape the way agents reason about truth and engage in dialogue with one another.

## Quick Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")             # starts in Ego
agent2 = Agent("A2", state="Jaz")

# Have a short discussion about "truth"
lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

Running this example prints how each agent responds and whether they transition to a new ontological state.

## Running the Tests

Unit tests are located under `tests/` and can be executed with `pytest`:

```bash
pytest
```

If you encounter import issues, you can invoke pytest as a module:

```bash
python -m pytest
```

The tests verify correct state transitions, agent responses, and the sample dialogue behaviour.
