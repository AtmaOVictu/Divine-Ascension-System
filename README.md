# Divine Ascension System

Divine Ascension System is a small experimental framework for simulating ontological agents. Each agent moves between three philosophical states—**Ego**, **Jaz**, and **Enotnost**—according to its emotional state and tension level. The package includes basic classes for agents, helper functions to create dialogues, and unit tests to verify behaviour.

## Installation

Clone the repository and install the project using `pip` in editable mode:

```bash
pip install -e .
```

No external dependencies are required beyond Python 3.8+.

## Usage

Create two agents and run a philosophical dialogue:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

This example shows how agents transition between states when emotion or tension thresholds are exceeded and how their responses reflect their current ontological state.

## Project Goals

* Demonstrate a simple ontological agent model.
* Provide a basis for experimenting with philosophical state transitions.

## Contributing

Issues and pull requests are welcome. Please run the unit tests before submitting changes:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
