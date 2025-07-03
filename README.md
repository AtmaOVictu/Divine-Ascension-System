# Divine-Ascension-System

This project implements a small agent-based framework where ontological agents debate philosophical truths. Agents evolve through three ontological states based on their emotional intensity and internal tension.

## Ontological States

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by our relationships.
- **Enotnost**: All truths are one, interconnected.

## State Transitions

An agent transitions when either of the following thresholds is exceeded:

- **Tension** greater than `0.7`
- **Emotion** greater than `0.5`

Transitions occur as follows:

- `Ego` → `Jaz`
- `Jaz` → `Enotnost`

Every transition is recorded in the agent's history so that the conversation flow can be analysed afterwards.

## Quick Example

Create two agents, run a dialogue and inspect their history:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Initialise agents
agent1 = Agent("A1")               # starts in Ego
agent2 = Agent("A2", state="Jaz")   # starts in Jaz

# Generate a short philosophical dialogue
conversation = philosophical_dialogue(agent1, agent2)
for line in conversation:
    print(line)

print("Agent1 history:", agent1.history)
print("Agent2 history:", agent2.history)
```

This will show each agent's responses based on their current state and reveal any transitions triggered by increasing emotion or tension.
