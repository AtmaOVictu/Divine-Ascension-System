from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions1: Tuple[float, str] | None = None,
    emotions2: Tuple[float, str] | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant.
    agent2 : Agent
        Second participant.
    emotions1 : Tuple[float, str] | None
        Optional emotion update for the first agent as ``(value, name)``.
    emotions2 : Tuple[float, str] | None
        Optional emotion update for the second agent as ``(value, name)``.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if emotions1:
        agent1.set_emotion(*emotions1)
    if emotions2:
        agent2.set_emotion(*emotions2)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
