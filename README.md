# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Running Tests

Directly executing `pytest` may fail because the package modules are not
automatically discoverable. Ensure Python can resolve the `divine_agents`
package by either setting `PYTHONPATH` or invoking pytest as a module.

```bash
# Option 1: adjust PYTHONPATH
PYTHONPATH=. pytest -q

# Option 2: run pytest as a module
python -m pytest -q
```

Either approach allows the tests under `tests/` to run successfully.
