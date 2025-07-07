# Divine-Ascension-System

Divine-Ascension-System is a minimal framework for simulating philosophical agents that evolve through three ontological states:

- **Ego**: truth is absolute and independent of others.
- **Jaz**: truth is relative and shaped by our relationships.
- **Enotnost**: all truths are unified and interconnected.

Agents carry emotional and tension values. When tension exceeds `0.7` or emotion exceeds `0.5`, the agent transitions from **Ego** to **Jaz** or from **Jaz** to **Enotnost**. Dialogue between agents reflects their current state and emotional response.

## Installation

1. Clone this repository.
2. Ensure Python 3.8+ is installed.
3. (Optional) create and activate a virtual environment.
4. Install the project in editable mode:

```bash
pip install -e .
```

To run the unit tests use:

```bash
python -m unittest discover tests
```

## Usage Example

The following example creates two agents, triggers state transitions by raising their emotion levels, and runs a sample dialogue.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

# Raise emotions which also adjust tension
agent1.update_emotion(0.8)
agent2.update_emotion(0.6)

# Transition based on thresholds
agent1.transition()
agent2.transition()

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this will print the ontological state of each agent and how they perceive truth during the conversation.
