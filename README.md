# Divine-Ascension-System

This project contains simple ontological agents that transition between **Ego**, **Jaz**, and **Enotnost** states. Agents can participate in philosophical dialogues reflecting absolute, relative, or unified views on truth.

## MultiColor Agents

`MultiColorAgent` extends the basic agent with a color representation and a visibility flag. Colors correspond to the current state:

- **Ego**: Red
- **Jaz**: Blue
- **Enotnost**: Gold

Visibility toggles randomly between `Visible` and `Hidden` after each transition.

## Running Tests

Use `python -m pytest -q` to run the unit tests.
