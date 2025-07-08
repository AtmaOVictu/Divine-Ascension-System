# Divine Ascension System

This project demonstrates a simple agent-based model that explores three
ontological states: **Ego**, **Jaz**, and **Enotnost**. Agents transition between
these states based on their emotional intensity and tension levels. Through
dialogue they debate philosophical questions about absolute, relative and
unified truths.

## Setup

1. Clone the repository.
2. Install dependencies (none are required outside the Python standard
   library, but a recent Python 3 interpreter is needed).

## Running

The package exposes convenience imports. An example interactive session:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("Agent 1")
a2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(a1, a2, exchanges=3):
    print(line)
```

## Testing

Run unit tests using `pytest`:

```bash
python -m pytest -q
```

## Core Concepts

- **Ego (⊘)** – truth is absolute and independent of others.
- **Jaz (∫(dru/x))** – truth is relative and shaped by relationships.
- **Enotnost (RES001)** – all truths are one and interconnected.

Emotions and tension influence how agents move through these states and how
they respond in dialogue.

