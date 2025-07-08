# Divine-Ascension-System

Divine-Ascension-System is a small Python package for experimenting with ontological agents. Each agent moves through a philosophical model of three states:

1. **Ego** – the agent sees truth as absolute and independent of others.
2. **Jaz** – the agent begins to recognise that truth is relative and shaped by relationships.
3. **Enotnost** – the agent realises that all truths are unified and interconnected.

State transitions occur when an agent's **tension** exceeds `0.7` or its **emotion** exceeds `0.5`. Agents can therefore evolve from `Ego` → `Jaz` → `Enotnost` during interaction.

## Installation

Clone the repository and install the dependencies with `pip`:

```bash
git clone https://github.com/your-username/Divine-Ascension-System.git
cd Divine-Ascension-System
pip install -r requirements.txt  # or install numpy and pytest manually
```

## Usage example

The package exposes an `Agent` class and a `philosophical_dialogue` helper. The snippet below demonstrates creating two agents and simulating a short conversation:

```python
from divine_agents import agent, dialogue

# create agents with initial states and emotions
a1 = agent.Agent("Agent 1", emotional_state="Ego", tension=0.6, emotion=0.4)
a2 = agent.Agent("Agent 2", emotional_state="Jaz", tension=0.7, emotion=0.5)

lines = dialogue.philosophical_dialogue(a1, a2)

for line in lines:
    print(line)
```

The conversation updates each agent's emotion, possibly triggering a transition to the next ontological state.

## Running the tests

Unit tests live in the `tests/` directory and can be executed with:

```bash
python -m pytest
```

They cover basic state transitions and the dialogue function.

## License

This project is released under the MIT License.

