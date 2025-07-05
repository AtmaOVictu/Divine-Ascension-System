# Divine-Ascension-System

## Overview
This project models a simple ontological framework where agents transition through philosophical states based on emotion and tension. Each agent reflects one of three principles:

- **Ego**: truth is absolute and independent of others.
- **Jaz**: truth is relative and shaped by relationships.
- **Enotnost**: all truths are one and interconnected.

Agents engage in short dialogues and may shift state when tension exceeds `0.7` or emotion exceeds `0.5`. Unit tests verify state transitions and responses.

## Installation
1. Clone this repository.
2. (Optional) create and activate a virtual environment.
3. Expose the project on `PYTHONPATH` so the tests can resolve imports:

```bash
export PYTHONPATH=$(pwd)
```

There are no additional dependencies.

## Running Tests
After fixing the import path, run the tests with `pytest`:

```bash
python -m pytest
```

Add `-q` for concise output.
