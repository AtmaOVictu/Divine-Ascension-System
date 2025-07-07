# Divine-Ascension-System

The Divine-Ascension-System simulates interactions between philosophical agents.
Agents transition between ontological states (**Ego**, **Jaz**, **Enotnost**) based
on their emotional intensity and tension. Each state reflects a specific view on
truth which shapes the dialogue among agents.

## Installation

The project has no external dependencies. Clone the repository and ensure
Python 3.11+ is available.

```bash
python -m venv venv
source venv/bin/activate
```

## Running Tests

Unit tests validate state transitions and dialogue behaviours. Execute them with:

```bash
pytest -q
```

## Usage Example

```python
from divine_agents import Agent, philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz", emotion_type="joy")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

The dialogue output will show how emotional shifts cause agents to transition
between ontological states while debating absolute, relative and unified truths.
