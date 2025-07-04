# Divine-Ascension-System

This project simulates interactions between ontological agents moving through three states: **Ego**, **Jaz**, and **Enotnost**. Agents transition between these states based on their emotional intensity and accumulated tension, reflecting different philosophical perspectives on truth.

## Features

- **Dynamic state transitions** driven by emotion and tension levels.
- **Philosophical dialogue** generation showing how each state views truth.
- **Unit tests** verifying state changes and dialogue logic.

## Usage

1. Create agents and initiate a dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

2. Agents update their emotion or tension, triggering transitions when thresholds are met (tension > `0.7` or emotion > `0.5`).

## Running Tests

Run the included unit tests with:

```bash
python -m unittest discover -s tests
```

The tests cover state transitions, agent responses, and dialogue output.

## Notes on `TESTI.ipynb`

The repository previously contained a placeholder notebook named `TESTI.ipynb` with no content. It has been removed as it served no purpose in the current project structure.

