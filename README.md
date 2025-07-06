# Divine-Ascension-System

An interactive framework for simulating ontological agents. Each agent evolves
through the states **Ego**, **Jaz** and **Enotnost**, guided by its emotional
intensity and tension level. Agents discuss philosophical concepts and make
moral decisions according to their state.

## Installation

Clone the repository and install dependencies:

```bash
git clone <repo-url>
cd Divine-Ascension-System
pip install -r requirements.txt  # if a requirements file is provided
```

## Running

Execute the dialogue example:

```bash
PYTHONPATH=. python -m divine_agents.dialogue
```

## Testing

Run the unit tests:

```bash
PYTHONPATH=. pytest -q
```

## Documentation

See [AGENTS.md](AGENTS.md) for an overview of agent design, state transitions
and testing guidelines.
