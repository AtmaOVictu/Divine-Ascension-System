# Codex: Divine Ascension System

Codex is a dynamic agent-based framework for exploring philosophical transitions between the states **Ego**, **Jaz**, and **Enotnost**. Each agent carries an emotional profile and a level of tension that drives how it responds in dialogues and when it shifts ontological phases.

## Features

### Dynamic Agents
- Agents transition between **Ego**, **Jaz**, and **Enotnost**.
- Emotions directly influence tension and interactions.

### Real-Time Updates
- Parameters such as tension or emotion can be adjusted instantly.
- Visual or textual traces show how transitions unfold.

### Ontological Phases
- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative and shaped by relationships.
- **Enotnost** – all truths become one, interconnected.

### Simulation and Testing
- Sample dialogues demonstrate how agents debate absolute, relative, and unified truths.
- Unit tests validate state transitions and philosophical responses.

## System Planning
Interactive programming enables instant feedback while experimenting with agent parameters. Tension and emotion determine when an agent moves from **Ego** to **Jaz** or from **Jaz** to **Enotnost**. Oppositions (or "shadows") help reveal new dimensions within transitions.

## Requirements and Installation
- Python 3.6+
- `pytest` for testing

Install dependencies and run tests with:
```bash
git clone https://github.com/your-username/codex.git
cd codex
pip install -r requirements.txt
PYTHONPATH=. pytest -q
```

## Usage
Create agents and run a dialogue:
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This example shows how the emotional intensity triggers state transitions and shapes philosophical answers.

## Testing
Run all tests with:
```bash
PYTHONPATH=. pytest -q
```

To run a specific test module:
```bash
PYTHONPATH=. pytest tests/test_agents.py
```

## Extending the Project
The system can be expanded with new ontological phases or additional emotional dynamics. By keeping the code modular, you can adapt dialogue patterns or transition rules to explore new ideas.

