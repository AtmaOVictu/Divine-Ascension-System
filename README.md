# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

This project models agents that transition between three ontological states:
**Ego**, **Jaz**, and **Enotnost**. Emotions and tension determine how agents
evolve and how they respond during philosophical dialogue.

## Features

- **State transitions** driven by emotion (>0.5) or tension (>0.7).
- **Dialogue simulation** where agents debate absolute, relative and unified
  truths.
- **Unit tests** ensure transitions and responses behave as expected.

## Usage

Clone the repository and install the dependencies (Python 3.11 or later).

```bash
git clone <repo-url>
cd Divine-Ascension-System
python -m pytest -q
```

To experiment with the dialogue logic, open a Python shell:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2, rounds=2):
    print(line)
```

The output illustrates how each agent's emotional state influences their
transition from Ego to Jaz or Jaz to Enotnost while discussing truth.
