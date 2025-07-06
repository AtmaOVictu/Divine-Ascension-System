# Divine-Ascension-System

Divine-Ascension-System is a simple simulation of philosophical agents. Each agent
occupies an ontological state that guides how they perceive truth and how they
respond in dialogue. Agents may transition between states when emotions or
tension reach defined thresholds, allowing basic explorations of dynamic
philosophical debate.

## Ontological Model

Agents exist in one of three states:

| State    | Principle                                                         |
|----------|------------------------------------------------------------------|
| **Ego**  | Truth is absolute and independent of others.                      |
| **Jaz**  | Truth is relative, shaped by relationships and experiences.       |
| **Enotnost** | All truths are one and interconnected. Separation is illusion. |

Transitions occur when an agent's tension exceeds **0.7** or their emotion
exceeds **0.5**:

```
agent.update_tension(0.8)
agent.transition()  # => "Jaz"
```

## Setup

1. Ensure Python 3.11+ is installed.
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install `pytest` for running tests:

   ```bash
   pip install pytest
   ```

## Running Tests

The tests expect the project directory to be on `PYTHONPATH`. From the project
root run:

```bash
PYTHONPATH=. pytest -q
```

or using the standard library:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

## Example Interaction

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# two agents in different states
ego_agent = Agent("A1")                    # starts in Ego
jaz_agent = Agent("A2", state="Jaz")       # starts in Jaz

# run a short dialogue and print each line
for line in philosophical_dialogue(ego_agent, jaz_agent):
    print(line)
```

Example output might look like:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

This illustrates how emotional changes cause state transitions and how responses
reflect the philosophical stance of each state.
