# Divine-Ascension-System

This repository contains a simple ontological agent framework. Agents can inhabit one of three states and transition between them based on emotion and tension:

- **Ego** – truth is absolute and independent.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

## Creating Agents

```python
from divine_agents.agent import Agent

agent = Agent("A1")
print(agent.state)  # Ego

# Increase emotion to trigger a transition
agent.update_emotion(0.8)
new_state = agent.transition()
print(new_state)  # Jaz
```

You can also trigger transitions using tension:

```python
agent2 = Agent("B")
agent2.update_tension(0.9)
agent2.transition()  # Jaz
```

## Running a Sample Dialogue

The package provides a helper to simulate a dialogue between two agents.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

first = Agent("A1")
second = Agent("A2", state="Jaz")

for line in philosophical_dialogue(first, second):
    print(line)
```

During the conversation each agent updates its emotion, leading to state transitions where appropriate.

## Running Tests

Execute the unit tests with:

```bash
python -m pytest -q
```

The tests validate state transitions, emotional influence and dialogue output.

