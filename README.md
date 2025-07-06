# Divine-Ascension-System

The **Divine-Ascension-System** is a simple framework for experimenting with ontological agents. Each agent progresses through three philosophical states—**Ego**, **Jaz**, and **Enotnost**—depending on their emotional intensity and tension.

Agents can engage in short dialogues discussing the nature of truth. State transitions occur when an agent's tension exceeds `0.7` or their emotion exceeds `0.5`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Divine-Ascension-System.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # if requirements are defined
   ```
3. Run the sample dialogue:
   ```bash
   python -m divine_agents.dialogue
   ```

## Running Tests
Execute all unit tests using:
```bash
python -m unittest discover -s tests
```

## Project Structure
- `divine_agents/agent.py` – agent implementation and transition logic.
- `divine_agents/dialogue.py` – helper for simulating philosophical conversations.
- `tests/` – unit tests verifying transitions and responses.
- `AGENTS.md` – detailed specification of agent behaviour.

## Example
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent A")
agent2 = Agent("Agent B", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
