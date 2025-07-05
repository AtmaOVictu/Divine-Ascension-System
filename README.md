# Divine-Ascension-System

This project demonstrates a minimal agent framework built on an ontological
model with three states:

* **Ego** – truth is absolute.
* **Jaz** – truth is relative and shaped by relations.
* **Enotnost** – truth is unified and interconnected.

Agents transition between these states when their tension exceeds `0.7` or their
emotion exceeds `0.5`. A small dialogue module lets two agents debate the nature
of truth in either Slovenian (`"sl"`) or English (`"en"`).

## Usage

Run the philosophical dialogue demo:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2, lang1="en", lang2="sl"):
    print(line)
```

## Tests

Install `pytest` (if not already available) and run:

```bash
python -m pytest -q
```

The tests verify state transitions, clamping of tension/emotion values and the
multilingual dialogue responses.
