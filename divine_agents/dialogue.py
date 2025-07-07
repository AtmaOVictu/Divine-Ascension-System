from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_inc1: float = 0.8,
    emotion_inc2: float = 0.6,
    tension_inc1: float = 0.0,
    tension_inc2: float = 0.0,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First agent participating in the dialogue.
    agent2 : Agent
        Second agent participating in the dialogue.
    emotion_inc1 : float, optional
        Emotion increment applied to ``agent1``.
    emotion_inc2 : float, optional
        Emotion increment applied to ``agent2``.
    tension_inc1 : float, optional
        Additional tension increment for ``agent1``.
    tension_inc2 : float, optional
        Additional tension increment for ``agent2``.
    """
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(emotion_inc1)
    if tension_inc1:
        agent1.update_tension(agent1.tension + tension_inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion_inc2)
    if tension_inc2:
        agent2.update_tension(agent2.tension + tension_inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
