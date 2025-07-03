# Divine-Ascension-System

This project provides a minimal framework for simulating ontological agents
that transition between three philosophical states: **Ego**, **Jaz** and
**Enotnost**.  Each agent holds an emotional intensity and tension level which
influence its state.  When the tension exceeds `0.7` or the emotion exceeds
`0.5`, the agent transitions from `Ego` → `Jaz` → `Enotnost`.

## Usage

### Creating an agent

```python
from divine_agents.agent import Agent

agent = Agent("Ada")
agent.update_emotion(0.8)
agent.transition()  # -> "Jaz"
```

### Running a dialogue

`philosophical_dialogue` allows two agents to exchange a few lines that reflect
their current state.  The function returns the dialogue as a list of strings.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

### Running tests

All unit tests can be executed with:

```bash
python -m pytest -q
```

The tests verify state transitions, responses and the dialogue utility.
