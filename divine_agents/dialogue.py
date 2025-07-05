from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    rounds: int = 2,
    emotion_delta: float = 0.3,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round both agents respond to the same question, their emotional
    intensity rises and a possible state transition is triggered.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"
    for _ in range(rounds):
        lines.append(agent1.interact(question, emotion_delta))
        lines.append(agent2.interact(question, emotion_delta))
    return lines
