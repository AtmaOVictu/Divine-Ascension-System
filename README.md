# Divine-Ascension-System

This project provides a simple ontological framework where agents move between the
states **Ego**, **Jaz**, and **Enotnost** depending on their emotional intensity
and tension levels. The `Agent` class in `divine_agents/agent.py` contains the
logic for adjusting emotion, tension, and performing state transitions when the
thresholds are exceeded.

A small example of a philosophical dialogue can be found in
`divine_agents/dialogue.py`. It demonstrates how two agents interact and evolve
through a short conversation while reflecting their current philosophical views.

## Running the tests

To run the unit tests, first install `pytest` and then invoke `pytest` from the
repository root:

```bash
pip install pytest
pytest
```
