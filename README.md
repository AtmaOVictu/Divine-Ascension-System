# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Purpose
The Divine-Ascension-System showcases agents that move through the ontological
states of **Ego**, **Jaz**, and **Enotnost**. Agents shift when their emotional
intensity or tension exceeds preset thresholds, letting you explore dialogues
that contrast absolute, relative, and unified truths.

## Installation
Clone the repository and optionally install the package in editable mode:

```bash
git clone <repo-url>
cd Divine-Ascension-System
pip install -e .
```

## Running the sample dialogue
Run the snippet below to start a short conversation between two agents:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running the tests
Execute the test suite with:

```bash
python -m pytest
```

After Issue 1 is resolved you can also use `pytest` directly.
