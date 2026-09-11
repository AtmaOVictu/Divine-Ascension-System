from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    emotion_step1: float = 0.8,
    emotion_step2: float = 0.6,
    exchanges: int = 1,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters allow customizing emotion increases for each agent and the
    number of exchanges performed.
    """
    lines: List[str] = []
    for _ in range(exchanges):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(emotion_step1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emotion_step2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
