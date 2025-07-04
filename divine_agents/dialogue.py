from typing import List, Iterable, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    updates: Iterable[Tuple[Agent, str, float]] | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        The interacting agents.
    updates:
        Optional sequence of emotion updates in the form
        ``(agent, emotion_type, intensity)``. If ``None`` a default
        sequence is used.
    """

    if updates is None:
        updates = [
            (agent1, "anger", 0.8),
            (agent2, "joy", 0.6),
        ]

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for ag, etype, value in updates:
        ag.update_emotion(etype, value)
        lines.append(f"{ag.name} prehaja v stanje: {ag.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
