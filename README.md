# Divine-Ascension-System

This project demonstrates a minimal agent based framework where agents
transition between the philosophical states **Ego**, **Jaz** and
**Enotnost**. Transitions depend on the current *tension* and *emotion*
of each agent. Agents also discuss truth according to their state.

## Installation

The system requires **Python 3.8+** and only uses the Python standard
library. For best isolation create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

No additional dependencies are needed.

## Running the tests

All unit tests live in the `tests/` folder. Execute them with:

```bash
python -m pytest -q
```

## Usage example

The snippet below shows a short dialogue and the automatic state
transitions triggered by emotional intensity or tension levels.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")                # starts in Ego
agent2 = Agent("A2", state="Jaz")    # starts in Jaz

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Under optimal conditions a transition occurs whenever an agent's tension
exceeds **0.7** or its emotional intensity exceeds **0.5**. Emotions
such as `fear`, `anger`, `joy` or `sorrow` will respectively increase or
decrease tension when applied through `update_emotion`.
