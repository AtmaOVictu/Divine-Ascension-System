from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           emotions: Iterable[tuple[float, float]] | None = None) -> List[str]:
    """Simulate a dialogue where emotions drive state transitions.

    Parameters
    ----------
    agent1, agent2:
        Interacting agents.
    emotions:
        Optional iterable of ``(e1, e2)`` tuples describing emotion updates for
        each exchange. If ``None`` a single step will be performed.

    Returns
    -------
    List[str]
        Dialogue lines documenting states, transitions and responses.
    """

    lines: List[str] = []
    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if emotions is None:
        emotions = [(0.8, 0.6)]

    for e1, e2 in emotions:
        agent1.update_emotion(e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
