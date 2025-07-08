# Divine-Ascension-System

This project simulates philosophical agents that transition between
three ontological states based on their emotions and tension levels.

## Philosophical States

- **Ego (⊘)**: Truth is *absolute* and independent of others.
- **Jaz (∫(dru/x))**: Truth is *relative* and shaped by relationships.
- **Enotnost (RES001)**: Truth is *unified* and interconnected.

Agents move from **Ego** to **Jaz** or from **Jaz** to **Enotnost** when
`tension > 0.7` or `emotion > 0.5`.

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# create two agents in different states
agent1 = Agent("A1")  # default state Ego
agent2 = Agent("A2", state="Jaz")

# run a short dialogue
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Install dependencies (if any) and run the unit tests:

```bash
python -m unittest discover -s tests -v
```

This command executes the suite located in `tests/` and verifies
state transitions and dialogue responses.
