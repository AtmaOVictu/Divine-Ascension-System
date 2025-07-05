# Divine-Ascension-System

A minimal demonstration of ontological agents that transition between
``Ego``, ``Jaz`` and ``Enotnost`` states. Agents react to emotions and
tension and can participate in short philosophical dialogues.

## Running Tests

```bash
pytest -q
```

## Loading Simulation

The `simulate_loading` function illustrates a simple loading sequence
for an agent:

```python
from divine_agents.agent import Agent
from divine_agents.loading import simulate_loading

agent = Agent("Demo")
simulate_loading(agent, delay=0)
```
