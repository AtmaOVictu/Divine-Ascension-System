# Divine Ascension System

The Divine Ascension System is a minimal framework for exploring ontological agents that transition through three philosophical states: **Ego**, **Jaz**, and **Enotnost**. Agents respond to tension and emotion, allowing them to evolve during philosophical debates.

## Installation

The project uses only the Python standard library, so no additional packages are required. Ensure you have Python 3.8+ installed.

```bash
python --version
```

Clone the repository and install any optional dependencies using `pip` if they are added in the future.

## Running Tests

Unit tests are located in the `tests/` directory. Execute them with the built-in `unittest` runner:

```bash
python -m pytest -q
```

This command runs the entire test suite and reports the results.

## Example Usage

Below is a short example of creating two agents and starting a dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This will output the initial philosophical positions of each agent, trigger emotional updates, perform state transitions, and display how their responses change.

## Future Work

Planned extensions include specialised agent types such as `InsertionAgent` for dynamic dialogue insertion and more advanced conversation flows. Contributions are welcome.
