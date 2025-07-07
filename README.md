# Divine-Ascension-System

Divine-Ascension-System provides a lightweight agent framework that explores ontological states through philosophical dialogue. Each agent can hold one of three states—**Ego**, **Jaz**, or **Enotnost**—and transitions between these states are triggered by emotion and tension levels. The system allows experimentation with how emotions influence debates about absolute, relative, and unified truths.

## Ontological States

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by relationships.
- **Enotnost** – All truths are unified and interconnected.

Agents update their emotional intensity and tension. When the tension exceeds `0.7` or the emotion exceeds `0.5`, the agent will transition from Ego → Jaz or Jaz → Enotnost. Each state determines how the agent responds in a debate.

## Prerequisites

- Python 3.11 or later
- `pytest` for running the unit tests

Install `pytest` with:

```bash
pip install pytest
```

## Running the Tests

Run the unit tests from the repository root with `pytest` while ensuring that the project directory is on the `PYTHONPATH`:

```bash
PYTHONPATH=. pytest
```

All tests are located in the `tests` directory and check state transitions, responses, and dialogue output.

## Example Usage

The snippet below shows how to create two agents and start a philosophical dialogue between them:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Create agents in different ontological states
agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

# Start a dialogue
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Running this script will print the agents' initial answers, show how they transition based on emotion, and display their new responses.
