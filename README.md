# Divine Ascension System

A dynamic agent-based framework exploring philosophical dialogues and state transitions.

## Overview

Agents in this project embody three ontological states:

- **Ego**: Truth is absolute and independent.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: Truth is unified and interconnected.

Agents transition between these states based on their emotional intensity and tension levels. They engage in dialogues reflecting their current state and emotions.

## Installation

```bash
pip install .
```

## Usage Example

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Running Tests

Execute the test suite with:

```bash
pytest -q
```

## Project Goals

This repository serves as a sandbox for simulating philosophical debates and exploring how emotions can influence the perception of truth. The system is designed to be modular and easily extended.
