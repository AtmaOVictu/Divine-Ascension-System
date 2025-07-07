# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

The project contains a simple framework for modelling ontological agents.

## Creating Agents

`Agent` objects live in `divine_agents.agent` and start in the `Ego` state. They
can transition to `Jaz` or `Enotnost` when their tension or emotion exceeds the
required thresholds.

```python
from divine_agents.agent import Agent

ana = Agent("Ana")
ana.update_emotion(0.8)  # also raises tension
ana.transition()         # --> "Jaz"
print(ana.respond("Kaj je resnica?"))
```

## Example Dialogue

`philosophical_dialogue` demonstrates how two agents interact:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Run the unit tests with `pytest`:

```bash
python -m pytest
```

