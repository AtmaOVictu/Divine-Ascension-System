# Divine-Ascension-System

Divine-Ascension-System is an experimental framework for simulating ontological agents that transition through philosophical states (Ego, Jaz, Enotnost). Each agent carries a tension and emotion value that drive their state changes and dialogue about truth.

## Features

- **State Transitions** – Agents move from Ego → Jaz → Enotnost when tension (>0.7) or emotion (>0.5) exceed thresholds.
- **Philosophical Dialogue** – Agents discuss absolute, relative, and unified truths depending on their current state.
- **Emotion Tracking** – Emotional intensity affects tension and dialogue style.
- **History Recording** – Agents keep a history of all states they visit.
- **Unit Tests** – Basic tests verify transitions, responses and sample dialogues.

## Usage

1. Clone the repository:

```bash
git clone <repo_url>
cd Divine-Ascension-System
```

2. (Optional) Create a virtual environment and install requirements (no external packages are needed beyond Python's standard library).

3. Run a sample dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent1")
agent2 = Agent("Agent2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Project Structure

```
divine_agents/
    agent.py      # Agent class with state transitions and responses
    dialogue.py   # Dialogue utilities for interactions
tests/
    test_agents.py  # Unit tests for transitions and responses
```

## Testing

Run the tests with:

```bash
python -m unittest tests.test_agents -v
```

## License

This project is released under the MIT License.
