# Divine-Ascension-System

Minimal framework for simulating philosophical agents that transition between
ontological states based on emotion and tension.

## Usage

Install dependencies (if any) and run the unit tests:

```bash
pytest -q
```

Agents can be created and used directly:

```python
from divine_agents import Agent, philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
print(philosophical_dialogue(a1, a2))
```

