# Divine-Ascension-System

This repository contains a small framework for experimenting with ontological agents. Agents progress through three states—**Ego**, **Jaz**, and **Enotnost**—based on their emotional intensity and tension levels. The library can be used to simulate short philosophical dialogues and to observe state transitions.

## Creating agents

Agents are defined in `divine_agents.agent.Agent` and can be created by providing a name and optional initial state:

```python
from divine_agents.agent import Agent

agent1 = Agent("Ana")            # starts in Ego by default
agent2 = Agent("Bojan", state="Jaz")
```

## Triggering transitions

An agent transitions from **Ego** to **Jaz**, or from **Jaz** to **Enotnost**, when either their tension exceeds `0.7` or their emotion exceeds `0.5`:

```python
agent1.update_emotion(0.8)  # raises tension as well
new_state = agent1.transition()
print(new_state)  # "Jaz"
```

Tension can also be set directly with `update_tension()`.

## Running a dialogue

`divine_agents.dialogue.philosophical_dialogue` accepts two agents and returns the conversation lines illustrating their states and transitions:

```python
from divine_agents.dialogue import philosophical_dialogue

lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

## Example session

Running the snippet above produces output similar to:

```
Ana (Ego): Resnica je absolutna in neodvisna od drugih.
Bojan (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Ana prehaja v stanje: Jaz
Bojan prehaja v stanje: Enotnost
Ana: Resnica je relativna, oblikovana z našimi odnosi.
Bojan: Vse resnice so eno, medsebojno povezane.
```

## Running tests

The project includes unit tests located in the `tests/` directory. Execute them from the repository root with:

```bash
python -m pytest
```

The current test suite should pass without additional configuration.
