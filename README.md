# Divine-Ascension-System

This project simulates philosophical agents that evolve through three ontological states:

- **Ego**: Truth is *absolute* and independent of others.
- **Jaz**: Truth is *relative* and shaped by relationships.
- **Enotnost**: Truth is *unified*; all truths are interconnected.

Agents shift from one state to another when their **tension** exceeds `0.7` or their
**emotion** exceeds `0.5`.

## Running the dialogue example

Execute the sample dialogue from the project root:

```bash
python run_dialogue.py
```

The script prints a short conversation and shows how agents transition between
states based on their emotions.

## Running the tests

After the issue #1 fix (which ensures the package can be imported correctly),
you can run the unit tests with:

```bash
pytest -q
```

The tests verify state transitions, agent responses and the dialogue flow.
