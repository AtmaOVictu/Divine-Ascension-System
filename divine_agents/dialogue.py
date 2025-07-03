from typing import Callable, List
from random import random
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    steps: int = 2,
    emotion_generator: Callable[[], float] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each step agents state their view of truth, experience a change in
    emotion, and may transition to a new ontological state.
    """

    if emotion_generator is None:
        emotion_generator = random

    lines: List[str] = []
    for _ in range(steps):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(emotion_generator())
        agent2.update_emotion(emotion_generator())
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
