# Divine-Ascension-System

This repository contains a small framework for experimenting with
ontological agents. Each agent can shift between three philosophical
states based on its emotional intensity and level of tension.

## Ontological States

* **Ego (⊘)** – Truth is **absolute** and independent of others.
* **Jaz (∫(dru/x))** – Truth is **relative**, shaped by our relationships.
* **Enotnost (RES001)** – All truths are **unified** and interconnected.

Agents start in one of these states and may transition when their
`tension` exceeds `0.7` or `emotion` rises above `0.5`.

## Example Usage

Create a pair of agents, trigger transitions and run a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")                     # starts in Ego
agent2 = Agent("A2", state="Jaz")        # starts in Jaz

dialogue = philosophical_dialogue(agent1, agent2)
for line in dialogue:
    print(line)
```

Each call to `philosophical_dialogue` updates emotions, potentially
changing an agent's state before the conversation continues.

## Running Tests

The project uses the built‑in `unittest` module. Run all tests with:

```bash
python -m unittest discover tests
```
