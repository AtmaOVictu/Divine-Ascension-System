# Divine-Ascension-System

Minimal agent-based framework showcasing philosophical state transitions.

## Installation

The package can be installed in editable mode for development:

```bash
pip install -e .
```

## Usage

Agents transition between ontological states (`Ego`, `Jaz`, `Enotnost`)
based on their emotion and tension levels. A short dialogue can be
simulated using:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```

## Running Tests

Tests require `pytest` and can be executed from the repository root:

```bash
pytest -q
```

