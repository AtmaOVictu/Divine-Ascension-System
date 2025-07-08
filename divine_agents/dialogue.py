from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_increase: float = 0.3,
    exchanges: int = 3,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Conversing agents.
    emotion_increase : float, optional
        Amount by which each agent's emotion is increased after every exchange.
    exchanges : int, optional
        Number of dialogue exchanges.
    """
    lines: List[str] = []

    for _ in range(exchanges):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(emotion_increase)
        agent2.update_emotion(emotion_increase)

        agent1.transition()
        agent2.transition()

    return lines
