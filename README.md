# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Setup

1. Ensure you have **Python 3.9+** installed.
2. Clone the repository and install the package locally:

```bash
git clone <repo-url>
cd Divine-Ascension-System
pip install -e .
```

## Usage

### Creating Agents

```python
from divine_agents.agent import Agent

ego_agent = Agent("A1")
jaz_agent = Agent("A2", state="Jaz")
```

### Running a Dialogue

```python
from divine_agents.dialogue import philosophical_dialogue

lines = philosophical_dialogue(ego_agent, jaz_agent)
for line in lines:
    print(line)
```

### Executing Unit Tests

Run all tests from the repository root:

```bash
python -m unittest discover tests
```

