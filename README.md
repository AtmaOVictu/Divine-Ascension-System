# Divine-Ascension-System

A simple demonstration of an ontological agent framework. Agents move through
three philosophical states depending on their **tension** and **emotion** levels:

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are one and interconnected.

Agents transition from **Ego** to **Jaz** or from **Jaz** to **Enotnost** when
their tension is above `0.7` or their emotion exceeds `0.5`. During dialogue,
emotions influence the response each agent gives about the nature of truth.

## Installation

This project has no external dependencies. Clone the repository and ensure you
are running Python 3.11 or later:

```bash
python --version
```

## Running the Dialogue Example

You can run a short philosophical exchange using the `philosophical_dialogue`
function:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent1")
agent2 = Agent("Agent2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This will output something similar to:

```
Agent1 (Ego): Resnica je absolutna in neodvisna od drugih.
Agent2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Agent1 prehaja v stanje: Jaz
Agent2 prehaja v stanje: Enotnost
Agent1: Resnica je relativna, oblikovana z našimi odnosi.
Agent2: Vse resnice so eno, medsebojno povezane.
```

## Running Tests

Execute the unit tests with:

```bash
python -m pytest -q
```

These tests verify state transitions, agent responses, and the dialogue output.
