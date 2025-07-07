# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Testing

To run the unit tests, make sure the `divine_agents` package is discoverable by
`pytest`. You can do this in one of two ways:

1. Set the `PYTHONPATH` environment variable to the project root when running
   `pytest`:

   ```bash
   PYTHONPATH=. pytest
   ```

2. Alternatively, install the project in editable mode and run `pytest`
   normally:

   ```bash
   pip install -e .
   pytest
   ```

Either approach ensures that tests import the local package correctly.
