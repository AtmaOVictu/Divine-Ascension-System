# Divine-Ascension-System

This project demonstrates a simple agent-based framework for exploring ontological
states and philosophical dialogues. Agents can transition between the states
**Ego**, **Jaz**, and **Enotnost** based on their emotion and tension levels.

## Running Dialogues from the Command Line

A command line interface is provided to start a short philosophical dialogue
between two agents. You can specify the initial state, tension and emotion for
both agents:

```bash
python -m divine_agents.cli --name1 A1 --state1 Ego --tension1 0.8 --emotion1 0.2 \
                            --name2 A2 --state2 Jaz --tension2 0.6 --emotion2 0.3
```

The script will print a dialogue showing how the agents respond and transition
to new states when the specified thresholds are reached.
