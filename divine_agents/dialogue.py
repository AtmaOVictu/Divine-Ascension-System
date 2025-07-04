from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions1: Iterable[float] | None = None,
    emotions2: Iterable[float] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue with optional emotion updates.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    emotions1 : Iterable[float] | None, optional
        Sequence of emotion intensity updates for ``agent1``. If ``None`` a
        single update of ``0.8`` is applied.
    emotions2 : Iterable[float] | None, optional
        Sequence of emotion intensity updates for ``agent2``. If ``None`` a
        single update of ``0.6`` is applied.

    Returns
    -------
    List[str]
        Lines of dialogue representing the interaction.
    """

    emotions1 = list(emotions1) if emotions1 is not None else [0.8]
    emotions2 = list(emotions2) if emotions2 is not None else [0.6]

    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    max_len = max(len(emotions1), len(emotions2))
    for idx in range(max_len):
        if idx < len(emotions1):
            agent1.update_emotion(emotions1[idx])
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        if idx < len(emotions2):
            agent2.update_emotion(emotions2[idx])
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
