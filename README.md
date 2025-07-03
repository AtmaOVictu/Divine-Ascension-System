# Divine-Ascension-System

UX HUB FOR INTERACTIVE COMMAND/

This project provides a simple ontological agent-based system. Agents transition between philosophical states (Ego, Jaz, Enotnost) based on tension and emotion.

## Environment setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies (the project currently relies only on the Python standard library):

```bash
pip install -r requirements.txt  # if such a file is added
```

## Running tests

Execute the unit tests with:

```bash
python -m unittest discover -s tests
```

## Example usage

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
