# Divine-Ascension-System

This project implements a minimal agent-based model exploring ontological states
(`Ego`, `Jaz`, `Enotnost`). Agents transition between states when their
`tension` or `emotion` values cross predefined thresholds. Responses in the
dialogue depend on both the current state and emotional intensity.

## Usage

The repository requires Python 3.11 or later and has no external dependencies.
Clone the repository and run the examples or tests directly.

```
python -m divine_agents.dialogue
```

## Running the Tests

Use `pytest` to execute the unit test suite.

```
pytest -q
```

If you prefer, you can also invoke the test runner via Python:

```
python -m pytest -q
```

The tests verify state transitions, emotional responses, and a short
philosophical dialogue between agents.
