# Divine-Ascension-System

The Divine Ascension System simulates ontological agents who move through
three philosophical states—**Ego**, **Jaz**, and **Enotnost**—based on their
emotional intensity and internal tension. Each state encapsulates a view of
truth:

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are unified and interconnected.

Agents can engage in dialogue, and rising emotion or tension may trigger a
transition from Ego to Jaz or from Jaz to Enotnost. The system is implemented
in the `divine_agents` package with accompanying unit tests in `tests/`.

## Requirements

- Python 3.8 or newer
- `pytest` for running the tests (no other external dependencies)

## Setup

1. Install Python 3.8+.
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install `pytest` if it is not already available:

   ```bash
   pip install pytest
   ```

## Running Tests

Execute all unit tests using `pytest`:

```bash
python -m pytest
```

The tests verify correct state transitions and dialogue behaviour.
