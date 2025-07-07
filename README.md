# Divine-Ascension-System

The Divine Ascension System provides a small framework for simulating
ontological agents that transition between philosophical states.
Agents hold an emotional state and a tension level. When either the
emotion exceeds `0.5` or the tension exceeds `0.7`, the agent may
transition from **Ego** to **Jaz** or from **Jaz** to **Enotnost**.

## Basic Usage

Create agents using `divine_agents.agent.Agent` and update their emotion
or tension to trigger transitions. Each agent can respond to questions in
a manner that reflects its current philosophical stance.

```python
from divine_agents.agent import Agent

alice = Agent("Alice")
alice.update_emotion(0.8)
print(alice.transition())   # -> "Jaz"
print(alice.respond("Kaj je resnica?"))
```

### Philosophical Dialogue

Use `divine_agents.dialogue.philosophical_dialogue` to run a short
conversation between two agents. The function returns a list of dialogue
lines.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Unit tests verify state transitions, responses and sample dialogue. Run
all tests with:

```bash
python -m unittest discover tests
```
