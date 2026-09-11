from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_increase1: float = 0.8,
    emotion_increase2: float = 0.6,
    exchanges: int = 1,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        The interacting agents.
    emotion_increase1, emotion_increase2 : float, optional
        Emotion increments for each agent at every exchange.
    exchanges : int, optional
        How many back-and-forth exchanges occur.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for _ in range(exchanges):
        agent1.update_emotion(emotion_increase1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emotion_increase2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
