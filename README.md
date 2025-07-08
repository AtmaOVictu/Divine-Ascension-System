# Divine-Ascension-System

The **Divine-Ascension-System** is a small Python project that models ontological agents progressing through three philosophical states:

1. **Ego** – the view that truth is absolute and independent of others.
2. **Jaz** – truth becomes relative, shaped through relationships.
3. **Enotnost** – all truths are unified and interconnected.

Agents transition between these states when their **tension** exceeds `0.7` or their **emotion** rises above `0.5`. The framework allows agents to debate topics and adapt their worldview as their emotions change.

## Installation

Clone the repository and install dependencies with `pip`:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not available, install packages manually:

```bash
pip install numpy pytest
```

## Usage Example

The snippet below creates two agents and runs a short dialogue using the library's helper function:

```python
from divine_agents import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent 1", state="Ego", tension=0.6, emotion=0.4)
agent2 = Agent("Agent 2", state="Jaz", tension=0.7, emotion=0.5)

lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)

# Agents transition when emotion or tension thresholds are exceeded
agent1.update_emotion(0.8)
agent1.transition()
```

## Ontological Model

The project explores how conversations and emotions can lead an agent from **Ego** to **Jaz** and finally to **Enotnost**. Each state influences how an agent interprets truth and responds in dialogue:

- **Ego** – answers reflect certainty in an absolute truth.
- **Jaz** – answers acknowledge the relativity of truth.
- **Enotnost** – agents speak of a single, unified truth.

## Running Tests

Unit tests live in the `tests/` directory. Run them with:

```bash
python -m pytest
```

These tests verify that state transitions occur when thresholds are reached and that agents respond philosophically according to their current state.

---

This repository is distributed under the MIT license.
