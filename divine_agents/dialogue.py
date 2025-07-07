from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, emotion_inc1: float = 0.8, emotion_inc2: float = 0.6
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first conversational agent.
    agent2 : Agent
        The second conversational agent.
    emotion_inc1 : float, optional
        Increment applied to ``agent1``'s emotion level, by default ``0.8``.
    emotion_inc2 : float, optional
        Increment applied to ``agent2``'s emotion level, by default ``0.6``.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion_inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion_inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
