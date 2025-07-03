# Divine-Ascension-System

The Divine-Ascension-System demonstrates a small agent-based model built on an ontological framework. Agents transition between philosophical states (**Ego**, **Jaz**, **Enotnost**) depending on their emotional level and tension. Each state reflects a different view of truth ranging from absolute to unified.

## Requirements

- Python 3.8 or newer
- `pytest` (for running the test suite)

Install `pytest` with:

```bash
pip install pytest
```

## Example

Create two agents and run a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")           # starts in Ego
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running tests

To execute the unit tests run:

```bash
python -m pytest -q
```

The command above runs the entire suite and shows a concise output. For verbose output you can omit the `-q` flag.
