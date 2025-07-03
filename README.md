# Divine-Ascension-System

Divine-Ascension-System is a minimal framework for simulating agents that evolve through ontological states while engaging in philosophical dialogue. Each agent carries an emotional state and tension level that may trigger a transition from **Ego** to **Jaz** or from **Jaz** to **Enotnost**.

## Installation

The project has no third-party dependencies beyond Python 3. Clone the repository and ensure Python 3 is available in your environment.

```bash
# Example
python --version
```

## Usage

### Running a Dialogue Example

You can run an interactive demonstration by invoking the `philosophical_dialogue` function from a Python shell:

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

### Running Tests

Unit tests are located in the `tests` directory. Execute them with:

```bash
python -m unittest
```

## Ontological States

Agents progress through the following states:

- **Ego (⊘)** – Truth is absolute and independent of others.
- **Jaz (∫(dru/x))** – Truth is relative and shaped by relationships.
- **Enotnost (RES001)** – All truths are unified and interconnected.

A transition occurs when an agent's `tension` exceeds `0.7` or its `emotion` exceeds `0.5`. These thresholds ensure that emotional intensity or stress can move an agent from one state to the next.

## Purpose

The framework serves as a lightweight tool to explore how emotional dynamics and philosophical principles interact during dialogue. It can be extended to simulate debates and state changes among multiple agents.

