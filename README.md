# Divine-Ascension-System

This project simulates ontological agents that transition between three
philosophical states—**Ego**, **Jaz**, and **Enotnost**—based on their
emotions and tension. Agents engage in dialogue about truth, allowing the
system to explore concepts of absolute, relative and unified truth.

## Setup

1. Clone the repository.
2. Install dependencies (only the standard library is required for basic
   usage, but tests rely on `pytest`):

```bash
pip install -r requirements.txt  # if present
```

3. Run the dialogue simulation or unit tests as needed.

## Running Tests

Execute the test suite with:

```bash
python -m pytest
```

## Core Concepts

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative, shaped by relationships and interactions.
- **Enotnost** – all truths are one, interconnected.

Tension greater than `0.7` or emotion above `0.5` triggers transitions from
Ego → Jaz → Enotnost.
