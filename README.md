# Divine-Ascension-System

This project demonstrates a simple agent-based simulation grounded in a 
small ontological model. Agents transition between three philosophical
states – **Ego**, **Jaz** and **Enotnost** – according to their tension and
emotional intensity. Their emotional type colours each reply during a
philosophical dialogue.

## Installation

The project has no external dependencies. Clone the repository and make
sure you have Python 3.11 available.

```bash
python -m venv venv
source venv/bin/activate
pip install -U pip
```

## Running the tests

Unit tests verify state transitions, emotional responses and the dialogue
simulation. Run the test suite with:

```bash
pytest -q
```

## Usage

The package exposes the :class:`Agent` class and the
:func:`philosophical_dialogue` helper. A minimal example:

```python
from divine_agents import Agent, philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

The resulting dialogue will show how each agent evolves from their
initial ontological stance while expressing their current emotion.
