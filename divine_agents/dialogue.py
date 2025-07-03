from typing import List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: Optional[float] = None,
    emotion2: Optional[float] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    emotion1 : float, optional
        Emotion intensity to apply to ``agent1``. Defaults to ``0.8`` if
        not provided.
    emotion2 : float, optional
        Emotion intensity to apply to ``agent2``. Defaults to ``0.6`` if
        not provided.
    """
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    e1 = 0.8 if emotion1 is None else emotion1
    agent1.update_emotion(e1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    e2 = 0.6 if emotion2 is None else emotion2
    agent2.update_emotion(e2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
