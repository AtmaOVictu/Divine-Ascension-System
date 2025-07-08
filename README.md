# Divine-Ascension-System

Divine-Ascension-System is a minimal framework for simulating agent-based philosophical dialogues. Agents transition between ontological states based on emotion and tension, demonstrating how perspectives on truth evolve from an **Ego** standpoint toward **Jaz** and eventually **Enotnost**.

## Purpose

The project showcases a dynamic model where agents discuss absolute, relative and unified truths. It is meant for experimentation and educational exploration of philosophical interactions influenced by emotional intensity.

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Divine-Ascension-System

# (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# There are no external dependencies; tests require pytest
pip install pytest
```

## Basic Usage

Create agents and let them debate using the provided helper functions:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Two agents beginning at different states
alice = Agent("Alice")               # defaults to Ego
bob = Agent("Bob", state="Jaz")

# Generate a short dialogue and print the lines
for line in philosophical_dialogue(alice, bob):
    print(line)
```

Running this snippet will show how the agents' emotional updates cause them to transition through states and alter their responses.

## Running Tests

Ensure the repository root is on the Python path and execute pytest:

```bash
PYTHONPATH=. pytest
```

All tests should pass, verifying transitions and dialogue behaviour.

## Philosophical States Demonstrated

The system models three ontological phases:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative, shaped by relationships and interactions.
- **Enotnost** – truth is unified and all truths are interconnected.

`Agent` objects hold the current state, emotion and tension. The `transition` method moves an agent from **Ego** to **Jaz**, or from **Jaz** to **Enotnost**, whenever tension exceeds `0.7` or emotion exceeds `0.5`. The `respond` method supplies state-specific answers, while `philosophical_dialogue` in `divine_agents/dialogue.py` demonstrates these transitions through a short exchange.

