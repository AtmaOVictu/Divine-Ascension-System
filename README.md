# Divine-Ascension-System

Divine-Ascension-System is a small experimental framework for simulating agents that progress through philosophical states. Agents move from **Ego**, to **Jaz**, and eventually **Enotnost** according to their emotional intensity and tension levels. Each state represents a different view of truth and influences the dialogue between agents.

## Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")             # starts in Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running the Test Suite

The project includes a small unit test suite. Install `pytest` and run it from the repository root:

```bash
python -m pytest -q
```
