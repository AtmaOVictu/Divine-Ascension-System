# Divine-Ascension-System

## Project Overview

This project simulates philosophical interactions between ontological agents. Each `Agent` can be in one of three states:

- **Ego** – truth is considered absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents hold levels of **tension** and **emotion**. When tension exceeds `0.7` or emotion exceeds `0.5`, the agent transitions from **Ego** to **Jaz** or from **Jaz** to **Enotnost**. The `philosophical_dialogue` function demonstrates a short conversation where agents respond according to their current state and may transition as emotions rise.

## Getting Started

### Requirements

- Python 3.8 or newer
- `pytest` for running the tests (install via `pip install pytest`)

No additional dependencies are required as the project relies only on the Python standard library.

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

### Running the Tests

From the repository root, ensure the package is discoverable and run `pytest`:

```bash
export PYTHONPATH=$(pwd)
pytest -q
```

All tests should pass and demonstrate correct state transitions and dialogue responses.
