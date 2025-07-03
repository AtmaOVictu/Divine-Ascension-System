# Divine Ascension System

This project demonstrates a minimal agent-based system inspired by ontological
concepts. Agents can transition between philosophical states—**Ego**, **Jaz**, and
**Enotnost**—based on their emotional intensity and tension. The package allows
simulated dialogues where agents debate absolute, relative and unified truths.

## Philosophical States

- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative, shaped by our relationships.
- **Enotnost**: All truths are one, interconnected.

Transitions occur when an agent's tension exceeds `0.7` or emotion exceeds
`0.5`. During a dialogue, emotion values can be provided to influence these
transitions.

## Usage

Install the package in your environment (e.g., via `pip install -e .`), then run
a simple dialogue:

```python
from divine_agents import Agent, philosophical_dialogue

alice = Agent("Alice")
# Bob starts in the second state "Jaz"
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```

You can also specify custom emotion values:

```python
philosophical_dialogue(alice, bob, emotion1=0.9, emotion2=0.3)
```

## Running Tests

The repository includes unit tests verifying state transitions and dialogue
behaviour. Execute them with:

```bash
python -m pytest -q
```

Running plain `pytest -q` also works because tests modify `sys.path` to include
the project root.
