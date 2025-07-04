from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    emotion1: float = 0.8,
    tension1: float = 0.0,
    emotion2: float = 0.6,
    tension2: float = 0.0,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participating agent.
    agent2 : Agent
        Second participating agent.
    emotion1 : float, optional
        Emotion intensity to apply to *agent1*.
    tension1 : float, optional
        Additional tension adjustment for *agent1*.
    emotion2 : float, optional
        Emotion intensity to apply to *agent2*.
    tension2 : float, optional
        Additional tension adjustment for *agent2*.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion1)
    agent1.update_tension(agent1.tension + tension1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2)
    agent2.update_tension(agent2.tension + tension2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
