# Divine-Ascension-System

A small prototype demonstrating ontological agents that transition between the
states **Ego**, **Jaz**, and **Enotnost**. Transitions are triggered by emotion
and tension levels and reflected in the dialogue between agents.

## Features

- `Agent` dataclass storing emotional data, tension and history
- `MultiLayerTransitionSystem` for more complex transitions
- `ExperienceBasedLearning` simple reinforcement-like mechanic
- `PhilosophicalDialogue` for conversations influenced by emotions

## Testing

Run the unit tests with:

```bash
python -m unittest tests/test_agents.py -v
```
