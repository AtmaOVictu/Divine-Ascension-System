from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
    tension1: float | None = None,
    tension2: float | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    emotion1 : float, optional
        Emotion intensity applied to agent1 if ``tension1`` is not provided.
        Defaults to ``0.8`` for backward compatibility.
    emotion2 : float, optional
        Emotion intensity applied to agent2 if ``tension2`` is not provided.
        Defaults to ``0.6`` for backward compatibility.
    tension1 : float or None, optional
        If provided, directly sets the tension for ``agent1`` before
        transition. When ``None`` the ``emotion1`` adjustment is used
        instead.
    tension2 : float or None, optional
        If provided, directly sets the tension for ``agent2`` before
        transition. When ``None`` the ``emotion2`` adjustment is used
        instead.
    """

    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    if tension1 is not None:
        agent1.update_tension(tension1)
    else:
        agent1.update_emotion(emotion1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    if tension2 is not None:
        agent2.update_tension(tension2)
    else:
        agent2.update_emotion(emotion2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
