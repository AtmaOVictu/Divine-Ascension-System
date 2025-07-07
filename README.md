# Divine-Ascension-System

This project demonstrates a small ontological agent framework. Agents can move 
between the states **Ego**, **Jaz**, and **Enotnost** based on their emotional 
intensity and tension. A simple dialogue engine showcases how two agents discuss
philosophical truths while their emotions influence state transitions.

## Features
- **Ontological agents** that hold a state and emotional tension
- **State transitions** from Ego → Jaz → Enotnost once thresholds are exceeded
- **Philosophical dialogues** illustrating how agents respond from each state
- **Unit tests** verifying transitions and responses

## Installation
The project requires Python 3. There are no third-party package dependencies.
Optionally create a virtual environment and then install the package in editable
mode:

```bash
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Running tests
Execute all unit tests using `unittest`:

```bash
python -m unittest discover tests
```

## Example dialogue
A small script in `examples/run_dialogue.py` prints a short interaction:

```bash
python examples/run_dialogue.py
```

This will display the philosophical discussion and show how the agents change
state as their tension increases.
