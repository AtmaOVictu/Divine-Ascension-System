# Divine-Ascension-System
This project provides a simple ontological framework for experimenting with
agent-based philosophical dialogues.

## Usage

Create agents and update their emotional state or tension to trigger
transitions. Every transition is timestamped and stored in
`Agent.transition_history`.

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

dialogue_lines = philosophical_dialogue(agent1, agent2)
for line in dialogue_lines:
    print(line)

print(agent1.transition_history)
```

The timestamps make it easy to insert your own time structure or to analyse
how agents evolve over time.
