# Divine-Ascension-System

A simple framework for simulating ontological agents that transition between
philosophical states. Agents respond according to their current state and can
engage in dialogues that adjust their emotional tension.

## Features

- **Agent** class with emotion and tension attributes
- State transitions based on tension (>0.7) or emotion (>0.5)
- Short and multi-turn philosophical dialogues
- Unit tests verifying transitions and responses

## Usage

```python
from divine_agents import Agent, philosophical_dialogue, multi_turn_dialogue

# create agents
agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

# single round dialogue
lines = philosophical_dialogue(agent1, agent2)

# multi-turn dialogue
more_lines = multi_turn_dialogue(agent1, agent2, rounds=2)
```
