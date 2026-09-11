from typing import List

from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
    exchanges: int = 2,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    emotion1 : float, optional
        Emotion increment for agent1 each exchange.
    emotion2 : float, optional
        Emotion increment for agent2 each exchange.
    exchanges : int, optional
        How many dialogue rounds to perform.
    """

    lines: List[str] = []
    for _ in range(exchanges):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(emotion1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emotion2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
