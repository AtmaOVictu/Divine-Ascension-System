# Divine-Ascension-System

The **Divine-Ascension-System** is a minimal Python project that models
ontological agents. Each agent carries an emotional state and can move
through philosophical phases—**Ego**, **Jaz**, and **Enotnost**—as their
tension or emotion increases. The system demonstrates how dialogue and
emotion influence an agent's view of truth:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by our relations.
- **Enotnost** – all truths are unified and interconnected.

Agents interact through short philosophical dialogues where their
emotions may trigger a transition from one state to the next.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Divine-Ascension-System
   ```

2. Install the required packages. This project only needs `pytest` for
   running the tests, so you can install it with:

   ```bash
   pip install pytest
   ```

   If you want to run the project as a package, ensure the repository
   root is on your `PYTHONPATH` or install it in editable mode:

   ```bash
   pip install -e .
   ```

## Usage Example

Below is a short example demonstrating how to create two agents and
invoke the dialogue function:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create two agents in different starting states
agent1 = Agent("Agent 1", state="Ego", tension=0.6, emotion=0.4)
agent2 = Agent("Agent 2", state="Jaz", tension=0.7, emotion=0.5)

# Run a philosophical dialogue between them
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

The dialogue shows how each agent responds according to its state and
how increased emotions push them toward the next phase.

## Running Tests

To execute the unit tests, make sure the repository root is on the
`PYTHONPATH` and run:

```bash
PYTHONPATH=. python -m pytest
```

The tests cover basic state transitions and dialogue responses.

