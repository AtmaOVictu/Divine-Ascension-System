# Divine Ascension System

This project simulates philosophical debates between ontological agents. Each agent can exist in one of three states:

- **Ego** – truth is absolute and independent.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

Agents transition between these states based on their emotional intensity and tension levels. The system provides utilities to trigger dialogues and observe how agents evolve during conversations.

## Installation

The package can be installed in editable mode using `pip`:

```bash
pip install -e .
```

## Usage Example

```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Run the unit tests with:

```bash
pytest -q
```

## Project Structure

- `divine_agents/` – core package containing the agent model and dialogue generator.
- `tests/` – unit tests verifying state transitions and dialogue responses.
- `setup.py` – packaging configuration for installation.

## Philosophical System

State transitions occur when an agent's `tension` exceeds **0.7** or `emotion` exceeds **0.5**. The responses for each state are:

- **Ego**: "Resnica je absolutna in neodvisna od drugih."
- **Jaz**: "Resnica je relativna, oblikovana z našimi odnosi."
- **Enotnost**: "Vse resnice so eno, medsebojno povezane."

These principles guide the dialogue generator and are validated through the unit tests.
