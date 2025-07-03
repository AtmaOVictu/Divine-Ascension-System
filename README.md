# Divine-Ascension-System

Divine-Ascension-System is a demonstration project showcasing a minimal
ontological agent framework. Agents are able to transition between three
philosophical states:

* **Ego** – truth is absolute and independent of others
* **Jaz** – truth is relative and shaped by relationships
* **Enotnost** – all truths are one and interconnected

An agent's state may change when its **tension** rises above `0.7` or its
**emotion** rises above `0.5`. These rules are implemented in
`divine_agents/agent.py`.

The repository also contains a tiny dialogue engine that lets two agents
discuss different views of truth while their emotions and tensions shift.

## Installation

```bash
git clone https://github.com/yourusername/Divine-Ascension-System.git
cd Divine-Ascension-System
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # file currently empty – no dependencies
```

## Running unit tests

Execute the following command from the repository root:

```bash
python -m unittest discover -s tests
```

The tests verify correct state transitions and dialogue responses.
