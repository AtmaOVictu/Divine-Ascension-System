# Divine-Ascension-System
A minimal framework for simulating ontological agents engaged in philosophical dialogue.

## Setup

Create and activate a virtual environment and install the test dependency:

```bash
python -m venv venv
source venv/bin/activate
pip install pytest
```

## Running tests

Execute the test suite with either command:

```bash
pytest
# or
python -m pytest
```

## Example usage

You can invoke a short dialogue between two agents in a Python session:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```
