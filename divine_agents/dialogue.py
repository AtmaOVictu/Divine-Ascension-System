from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
    exchanges: int = 1,
    question: str = "Kaj je resnica?",
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Interacting agents.
    emotion1, emotion2:
        Emotion increments applied to each agent per exchange.
    exchanges:
        Number of dialogue exchanges.
    question:
        The philosophical question discussed.
    """

    lines: List[str] = []
    for _ in range(exchanges):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.update_emotion(emotion1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emotion2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
