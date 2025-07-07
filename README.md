# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Overview
This project simulates philosophical agents that evolve through three ontological
states: **Ego**, **Jaz**, and **Enotnost**. Each agent carries tension and emotion
levels that determine how it views truth and how it transitions between states.

## Agent States
- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by our relationships.
- **Enotnost** – All truths are one and interconnected.

## State Transitions
Agents transition when emotional or tension thresholds are exceeded:
- `tension > 0.7` triggers a transition.
- `emotion > 0.5` also triggers a transition.

An agent moves from **Ego** to **Jaz**, and then from **Jaz** to **Enotnost**
when these thresholds are met.

## Example Usage
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")
for line in philosophical_dialogue(alice, bob):
    print(line)
```

## Installation
This repository uses only the Python standard library. Create a virtual
environment if desired and install Python 3.8 or newer. No extra packages are
required.

```bash
python -m venv venv
source venv/bin/activate
```

## Running Tests
Unit tests are located in the `tests/` directory. Execute them with:

```bash
python -m unittest discover
```

