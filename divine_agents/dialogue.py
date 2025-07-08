from typing import List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: Optional[float] = 0.8,
    emotion2: Optional[float] = 0.6,
    tension1: Optional[float] = None,
    tension2: Optional[float] = None,
    transitions: bool = True,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first agent participating in the dialogue.
    agent2 : Agent
        The second agent participating in the dialogue.
    emotion1 : float, optional
        Emotion intensity applied to ``agent1``. ``None`` skips the update.
    emotion2 : float, optional
        Emotion intensity applied to ``agent2``. ``None`` skips the update.
    tension1 : float, optional
        If provided, directly set tension level for ``agent1``.
    tension2 : float, optional
        If provided, directly set tension level for ``agent2``.
    transitions : bool, default ``True``
        If ``True`` perform state transitions for both agents after updates.
    """

    lines: List[str] = []
    # Initial responses from the current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Apply emotion and tension adjustments
    if emotion1 is not None:
        agent1.update_emotion(emotion1)
    if tension1 is not None:
        agent1.update_tension(tension1)

    if transitions:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    if emotion2 is not None:
        agent2.update_emotion(emotion2)
    if tension2 is not None:
        agent2.update_tension(tension2)

    if transitions:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses after potential state changes
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
