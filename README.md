# Divine-Ascension-System

This project simulates agent interactions within an ontological framework.
Agents transition through the philosophical states **Ego**, **Jaz**, and
**Enotnost** based on their emotional intensity and tension.  Each state
represents a different view of truth:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped through relationships.
* **Enotnost** – all truths are unified and interconnected.

The code provides a simple agent model and utilities for generating short
philosophical dialogues between agents.

## Installation

The system only relies on the Python standard library. Clone the repository and
ensure you have Python 3.11 or newer available.

```bash
git clone <repo-url>
cd Divine-Ascension-System
```

## Running Tests

Execute the unit test suite using `pytest`.

```bash
PYTHONPATH=. pytest -q
```

This command sets the Python path to the project root so that the `divine_agents`
package can be imported during testing.
