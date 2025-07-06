# Divine-Ascension-System

This project simulates ontological agents that can move between the states **Ego**, **Jaz** and **Enotnost**.  Agents change their state based on their emotional intensity and inner tension and engage in philosophical debates where they discuss absolute, relative and unified truths.

## Installation
Install dependencies using pip:
```bash
pip install -r requirements.txt  # if a requirements file is provided
```

## Usage
To run a simple simulation use:
```bash
python -m divine_agents.demo
```
You can also import the package and create agents directly in your own scripts:
```python
from divine_agents import Agent, philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Unit tests
Run the tests with:
```bash
python -m unittest discover
```

Feel free to fork the repository and submit pull requests for improvements.
