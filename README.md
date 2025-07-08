# Ontological Agent Simulation

This project implements a simple ontological agent system where agents
transition between the states **Ego**, **Jaz** and **Enotnost** based on
tension and emotion. Each agent can respond to philosophical questions and
participate in dialogues.

## Installation

Clone the repository and install the dependencies (none are currently
required beyond Python 3.11):

```bash
git clone <repository-url>
cd Divine-Ascension-System
```

## Running Tests

Use `pytest` to run the unit tests. The repository root is automatically
added to `PYTHONPATH` by the tests.

```bash
pytest -q
```

## Usage

The main classes live in `divine_agents`:

- `Agent`: represents an ontological agent with state, tension and emotion.
- `philosophical_dialogue`: helper that runs a short dialogue between two
  agents.

You can import them directly from the package:

```python
from divine_agents import Agent, philosophical_dialogue
```

## Project Structure

```
├── divine_agents
│   ├── __init__.py
│   ├── agent.py
│   └── dialogue.py
├── tests
│   └── test_agents.py
```

## License

MIT
