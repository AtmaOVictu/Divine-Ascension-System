# Divine-Ascension-System

This project models philosophical agents that transition between ontological states based on their emotions and tension levels. The states are **Ego**, **Jaz**, and **Enotnost**.

## Philosophical Framework

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are one and interconnected.

Agents begin in `Ego` and may transition to `Jaz` and then `Enotnost` when either
of the following thresholds are exceeded:

- **Tension > 0.7**
- **Emotion > 0.5**

## Setup

1. Clone the repository and navigate into it:

   ```bash
   git clone <repo-url>
   cd Divine-Ascension-System
   ```

2. Install Python 3.8+ and the (minimal) dependencies. This project has no
   external requirements beyond the standard library, but creating a virtual
   environment is recommended:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. (Optional) Install the project in editable mode if you wish to import it elsewhere:

   ```bash
   pip install -e .
   ```

## Usage Example

The core classes reside in `divine_agents`. Below is a minimal example of
creating two agents and letting them debate:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")            # starts in Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this will show how agents respond according to their current state and
how emotion updates cause transitions.

## Running Tests

Unit tests live in the `tests` directory. Run them with `unittest`:

```bash
python -m unittest discover tests
```

This verifies state transitions at the configured thresholds and ensures the
philosophical dialogue responds as expected.
