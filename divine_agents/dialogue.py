from typing import List, Iterable, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    increments: Iterable[Tuple[float, float]] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue and adjust emotions as it unfolds.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    increments:
        Iterable of ``(inc1, inc2)`` values determining how much emotion should
        be added to ``agent1`` and ``agent2`` at each dialogue step. If ``None``
        is provided a single step ``(0.8, 0.6)`` is used.
    """

    if increments is None:
        increments = [(0.8, 0.6)]

    lines: List[str] = []
    for inc1, inc2 in increments:
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(inc1)
        prev1 = agent1.state
        new1 = agent1.transition()
        if new1 != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")

        agent2.update_emotion(inc2)
        prev2 = agent2.state
        new2 = agent2.transition()
        if new2 != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
