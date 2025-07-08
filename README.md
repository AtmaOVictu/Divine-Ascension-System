# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Command Line Usage

Run a philosophical dialogue directly from the terminal:

```bash
python -m divine_agents.cli [--state1 STATE] [--state2 STATE] \
    [--tension1 VALUE] [--tension2 VALUE] \
    [--emotion1 VALUE] [--emotion2 VALUE]
```

This will create two agents and print each line of the dialogue. All parameters
are optional and default to the initial `Ego` state with zero tension and emotion.
