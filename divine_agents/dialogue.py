from typing import List, Iterable, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    interactions: Iterable[Tuple[float, float]] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue with configurable emotion updates.

    Parameters
    ----------
    agent1 : Agent
        First conversational agent.
    agent2 : Agent
        Second conversational agent.
    interactions : Iterable[Tuple[float, float]] | None, optional
        Sequence of ``(emotion1, emotion2)`` tuples. Each pair represents the
        emotion update for ``agent1`` and ``agent2`` for a single interaction
        step. When ``None``, a single step ``(0.8, 0.6)`` is used.
    """
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    if interactions is None:
        interactions = [(0.8, 0.6)]

    for emo1, emo2 in interactions:
        agent1.update_emotion(emo1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emo2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
