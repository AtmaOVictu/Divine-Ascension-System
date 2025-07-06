# Divine-Ascension-System

A small framework for simulating ontological agents that evolve through three philosophical phases: **Ego**, **Jaz**, and **Enotnost**. Agents respond to questions depending on their state and can transition to higher states when their internal **emotion** or **tension** passes defined thresholds.

## Features

- **Agent model** with tracked emotion, tension and state history.
- **State transitions** triggered when tension exceeds `0.7` or emotion exceeds `0.5`.
- **Philosophical dialogue** helpers to illustrate how agents debate absolute, relative and unified truths.
- **Unit tests** demonstrating transitions and dialogue output.

## Usage

Clone the repository and run the unit tests:

```bash
git clone <repo-url>
cd Divine-Ascension-System
python -m unittest discover
```

Example of creating two agents and running a dialogue:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(a1, a2):
    print(line)
```

## License

This project is released under the MIT License.
