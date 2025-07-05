from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
    tension1: float = 0.0,
    tension2: float = 0.0,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1: Agent
        First participant.
    agent2: Agent
        Second participant.
    emotion1: float, optional
        Emotion increment for ``agent1``. Defaults to ``0.8``.
    emotion2: float, optional
        Emotion increment for ``agent2``. Defaults to ``0.6``.
    tension1: float, optional
        Additional tension increment for ``agent1``.
    tension2: float, optional
        Additional tension increment for ``agent2``.
    """

    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion1, increment=True)
    if tension1:
        agent1.update_tension(tension1, increment=True)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2, increment=True)
    if tension2:
        agent2.update_tension(tension2, increment=True)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
