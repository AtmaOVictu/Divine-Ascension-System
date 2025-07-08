# Divine Ascension System

A Python framework for simulating ontological agents that evolve through the philosophical states **Ego**, **Jaz**, and **Enotnost**. Agents transition between these states based on their emotional intensity and tension.

## Setup

1. Clone the repository.
2. (Optional) Install dependencies: `pip install -r requirements.txt`.
3. Run unit tests with `python -m pytest`.

## Running a Simulation

Agents and dialogue utilities are exposed at the package root:

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2, emotion_increase=0.4, exchanges=2):
    print(line)
```

## Philosophical States

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by our relationships.
- **Enotnost** – All truths are one and interconnected.

Emotions and tension values between 0 and 1 determine how agents shift from **Ego** to **Jaz** and finally to **Enotnost**.
