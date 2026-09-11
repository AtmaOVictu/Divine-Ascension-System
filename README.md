# Divine-Ascension-System

Framework for simulating philosophical agents that move through three
ontological states: **Ego**, **Jaz**, and **Enotnost**. Agents transition
between these states based on their emotion and tension levels while
engaging in dialogues about absolute, relative and unified truths.

## Setup

1. Ensure you have Python 3.8+ installed.
2. Install dependencies (none external at the moment).

## Usage

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2, exchanges=2):
    print(line)
```

## Running Tests

Execute the test suite with:

```bash
python -m unittest discover -v
```

The tests verify state transitions, clamping of emotion and tension, and
that dialogue eventually leads agents toward higher states.
