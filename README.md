# Divine-Ascension-System

This project demonstrates a small agent framework where ontological agents
transition between three philosophical states: **Ego**, **Jaz**, and
**Enotnost**. Each agent carries a level of emotional intensity and tension
that may trigger a change of state. The accompanying `dialogue` module shows
how two agents debate the nature of truth while their emotional states evolve.

## Running the dialogue

Use the Python interpreter to execute a short dialogue between two agents. The
example below creates an agent in the `Ego` state and another in the `Jaz`
state and then prints the conversation:

```bash
python - <<'PY'
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
PY
```

Typical output looks like:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

## Running unit tests

Unit tests verify state transitions, agent responses, and the sample
dialogue. Execute them with `unittest`:

```bash
python -m unittest tests.test_agents
```

Successful output should report three passing tests.
