# Divine-Ascension-System

Divine-Ascension-System simulates philosophical agents transitioning through
different ontological states. Each agent's emotional intensity and tension
determine how they evolve from an Ego centric view to a unified Enotnost
perspective.

## Project Purpose

This project demonstrates a lightweight framework for exploring philosophical
dialogue and state changes in Python. Agents respond to questions and update
their ontological state based on emotion and tension thresholds. Unit tests are
provided to ensure these transitions work as expected.

## Ontological States

* **Ego** – Truth is absolute and independent of others.
* **Jaz** – Truth is relative and shaped by our relationships.
* **Enotnost** – All truths are one, interconnected.

Agents start in one of these states and may shift to the next when their
tension exceeds `0.7` or their emotion rises above `0.5`.

## Running Tests

Install any required dependencies and run the test suite with:

```bash
python -m unittest
```

## Example Usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents
a1 = Agent("A1")                # defaults to Ego state
a2 = Agent("A2", state="Jaz")   # start in Jaz

# Run a short dialogue and print the lines
for line in philosophical_dialogue(a1, a2):
    print(line)
```

This example shows how agents respond and transition between states as their
emotions and tension change.
