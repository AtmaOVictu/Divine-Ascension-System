from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float | None = None,
    emotion2: float | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first agent participating in the dialogue.
    agent2 : Agent
        The second agent participating in the dialogue.
    emotion1 : float, optional
        Emotion intensity for ``agent1``. If ``None`` the default of ``0.8`` is
        used.
    emotion2 : float, optional
        Emotion intensity for ``agent2``. If ``None`` the default of ``0.6`` is
        used.
    """
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8 if emotion1 is None else emotion1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6 if emotion2 is None else emotion2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
