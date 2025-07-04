# Divine-Ascension-System

This project provides a minimal framework for modelling philosophical agents that
transition between three ontological states:

* **Ego** – truth is absolute and independent of others.
* **Jaz** – truth is relative and shaped by relationships.
* **Enotnost** – all truths are unified and interconnected.

Agents transition when their tension exceeds `0.7` or their emotion exceeds
`0.5`. Each transition is stored in the agent's history only when a state
change occurs. Dialogue utilities demonstrate how agents in different states
respond to the question of truth.

## Usage

```
from divine_agents import Agent, philosophical_dialogue, SimulationEnvironment

# create agents
a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")

# run a short dialogue
lines = philosophical_dialogue(a1, a2)
for line in lines:
    print(line)

# run a simulation step
env = SimulationEnvironment()
env.add_agent(a1)
env.add_agent(a2)
env.run()
print(env.histories())
```

## Running Tests

Execute the unit tests with:

```
python -m unittest discover -s tests
```
