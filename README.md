# Divine-Ascension-System

This project models philosophical agents that evolve through three states:
**Ego**, **Jaz**, and **Enotnost**. Agents transition between these states when
their internal **tension** or **emotion** values exceed defined thresholds.
Dialogue between agents reflects their ontological stance and emotional state.

## Setup

The project requires Python 3.11 or later. Install dependencies (if any) and
run tests using `pytest`:

```bash
pip install -r requirements.txt  # if a requirements file exists
PYTHONPATH=. pytest -q
```

## Usage

The core functionality is provided by the `Agent` class and the
`philosophical_dialogue` function.

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
lines = philosophical_dialogue(a1, a2, exchanges=2)
for line in lines:
    print(line)
```

## Testing

Execute the unit tests with `pytest` as shown above. The tests verify state
transitions, responses, and dialogue progression.
