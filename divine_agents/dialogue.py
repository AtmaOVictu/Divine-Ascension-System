from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions1: Iterable[float] | None = None,
    emotions2: Iterable[float] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first agent participating in the dialogue.
    agent2 : Agent
        The second agent participating in the dialogue.
    emotions1 : Iterable[float] | None, optional
        Sequence of emotion values applied to ``agent1`` over the dialogue.
        If ``None``, a single value of ``0.8`` is used.
    emotions2 : Iterable[float] | None, optional
        Sequence of emotion values applied to ``agent2`` over the dialogue.
        If ``None``, a single value of ``0.6`` is used.

    Returns
    -------
    List[str]
        Dialogue lines describing state transitions and responses.
    """
    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Provide default emotion progressions if none are supplied
    if emotions1 is None:
        emotions1 = [0.8]
    if emotions2 is None:
        emotions2 = [0.6]

    for e1, e2 in zip(emotions1, emotions2):
        agent1.update_emotion(e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
