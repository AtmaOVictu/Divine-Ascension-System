# Divine Ascension System

This project simulates philosophical dialogue between agents that evolve through ontological states based on their emotional intensity and inner tension. Agents can occupy three states:

- **Ego** – Truth is viewed as absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships and interactions.
- **Enotnost** – All truths are unified and interconnected.

Transitions from one state to the next occur when an agent’s tension exceeds `0.7` or emotion exceeds `0.5`. The dialogue module demonstrates how emotions and tension influence a conversation about absolute, relative, and unified truths.

## Running the dialogue

From the repository root, start a Python interpreter and execute the following:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

This will print a short exchange showing how each agent’s state changes after their emotions are updated.

## Running the tests

Execute the unit tests with:

```bash
python -m pytest -q
```

The test suite checks state transitions, agent responses, and dialogue generation.

## Philosophy of transitions

Each ontological state represents a different view of truth. Agents begin in **Ego**, convinced that truth is absolute. Rising tension or emotion can move them to **Jaz**, where truth is seen as relative. Further intensity can elevate them to **Enotnost**, recognizing the unity of all truths. These philosophical principles drive the way agents argue and respond during the simulation.
