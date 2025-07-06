# Divine-Ascension-System

This project simulates agents that transition between three ontological states—**Ego**, **Jaz**, and **Enotnost**—according to their emotion and tension levels. Agents engage in philosophical dialogues reflecting absolute, relative, and unified truths. Emotional intensity and tension influence how agents respond and when they change state.

## Installation

Install the dependencies with pip:

```bash
pip install -r requirements.txt  # if a requirements file is provided
```

## Usage

Run the main simulation (if implemented) or import the package in your own scripts:

```bash
python main.py  # example entry point
```

You can also interact with the API directly:

```python
from divine_agents import Agent, philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")
conversation = philosophical_dialogue(alice, bob)
for line in conversation:
    print(line)
```

## Running Tests

Execute the unit tests with:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests to improve functionality or add new features.
