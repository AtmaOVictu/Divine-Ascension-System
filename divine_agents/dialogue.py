from typing import List

from .agent import Agent


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, *, emotion_increase: float = 0.8, exchanges: int = 2
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents participating in the conversation.
    emotion_increase:
        Amount by which each exchange increases emotion (and therefore
        tension). The value is clamped inside the agent.
    exchanges:
        Number of exchanges in the conversation.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(exchanges):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.update_emotion(emotion_increase)
        agent2.update_emotion(emotion_increase)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
