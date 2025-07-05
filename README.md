# Divine-Ascension-System

This project demonstrates a simple agent-based framework built around
ontological transitions. Agents move between three states—**Ego**, **Jaz** and
**Enotnost**—depending on their tension and emotion levels. Each agent can
respond to philosophical questions in either English or Slovenian and can take
part in a short dialogue simulation.

## Usage

The library requires Python 3.8 or later. To see a sample dialogue run:

```bash
python - <<'EOF'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1", language="en")
a2 = Agent("A2", state="Jaz", language="sl")
for line in philosophical_dialogue(a1, a2):
    print(line)
EOF
```

## Running Tests

To run the unit tests execute:

```bash
python -m pytest -q
```
