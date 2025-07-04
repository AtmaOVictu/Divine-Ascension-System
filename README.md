# Divine-Ascension-System

This project simulates philosophical agents that change their ontological
state based on emotion and tension. The system consists of a simple `Agent`
class and a `philosophical_dialogue` function that demonstrates how agents
interact.

## Agent States

Agents transition through three states:

- **Ego** – Truth is absolute and independent of others.
- **Jaz** – Truth is relative and shaped by our relationships.
- **Enotnost** – All truths are one and interconnected.

## State Transition Rules

An agent updates its `emotion` and `tension`. If the tension rises above
`0.7` or the emotion exceeds `0.5`, the agent transitions to the next
state in the sequence `Ego → Jaz → Enotnost`.

## Dialogue Demo

Run the following snippet to see agents converse and shift states:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Execute the unit tests with:

```bash
pytest -q
```

## Example Output

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```
