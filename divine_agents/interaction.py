"""Utilities for dynamic agent interaction."""
from typing import Iterable, List, Tuple

from .agent import Agent

EmotionStep = Tuple[Tuple[float, str], Tuple[float, str]]


def dynamic_dialogue(agent1: Agent, agent2: Agent, steps: Iterable[EmotionStep]) -> List[str]:
    """Run a dialogue where agents' emotions change over time.

    Each step contains emotion updates for both agents in the form
    ``((value1, name1), (value2, name2))``.
    After applying emotions, a state transition is attempted.
    """
    transcript: List[str] = []
    for (val1, name1), (val2, name2) in steps:
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(val1, name1)
        agent2.update_emotion(val2, name2)

        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    transcript.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    transcript.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return transcript
