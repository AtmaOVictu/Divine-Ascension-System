# Divine-Ascension-System

The Divine Ascension System explores philosophical dialogues between dynamic agents. Each agent can occupy one of three ontological states (**Ego**, **Jaz**, **Enotnost**) and transitions occur as emotion and tension rise during conversation. The goal of the project is to demonstrate how these agents reason about truth from different perspectives and how emotional factors drive their evolution.

## Installation

No external dependencies are required beyond Python 3. Simply clone the repository and ensure the project directory is on your `PYTHONPATH` so the `divine_agents` package can be imported.

```bash
git clone <repository-url>
cd Divine-Ascension-System
```

## Quickstart

Run the unit tests to verify the system works as expected:

```bash
python -m unittest discover tests
```

## Example Usage

Create two agents and run a short dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

The script prints the initial responses of each agent, shows how increased emotion triggers state transitions, and then prints their updated views on truth.

## Project Goals

This repository aims to provide a minimal, extensible framework for experimenting with philosophical state transitions and emotional dynamics in agent-based dialogues. Future work could expand the types of emotions and add richer conversational rules.
