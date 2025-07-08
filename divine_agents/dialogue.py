from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_a1: float = 0.8,
    emotion_a2: float = 0.6,
    exchanges: int = 1,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Interacting agents.
    emotion_a1, emotion_a2 : float
        Emotion increments applied to each agent per exchange.
    exchanges : int
        Number of conversational exchanges.
    """

    lines: List[str] = []
    for _ in range(exchanges):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

        agent1.update_emotion(emotion_a1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emotion_a2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond()}")
    lines.append(f"{agent2.name}: {agent2.respond()}")
    return lines
