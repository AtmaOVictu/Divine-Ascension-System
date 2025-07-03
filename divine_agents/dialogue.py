from typing import List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
    tension1: Optional[float] = None,
    tension2: Optional[float] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    emotion1 : float, optional
        Emotion intensity applied to ``agent1``. Defaults to ``0.8``.
    emotion2 : float, optional
        Emotion intensity applied to ``agent2``. Defaults to ``0.6``.
    tension1 : float, optional
        If provided, overrides ``agent1``'s tension value.
    tension2 : float, optional
        If provided, overrides ``agent2``'s tension value.
    """

    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion1)
    if tension1 is not None:
        agent1.update_tension(tension1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2)
    if tension2 is not None:
        agent2.update_tension(tension2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
