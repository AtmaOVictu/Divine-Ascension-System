from typing import List, Iterable, Tuple
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Backward compatible wrapper for a single-round debate."""
    return philosophical_debate(agent1, agent2, updates=[(0.8, 0.6)])


def philosophical_debate(agent1: Agent, agent2: Agent,
                          updates: Iterable[Tuple[float, float]]) -> List[str]:
    """Simulate a philosophical debate with given emotion updates.

    Parameters
    ----------
    agent1 : Agent
        First participant.
    agent2 : Agent
        Second participant.
    updates : Iterable[Tuple[float, float]]
        Sequence of emotion intensity updates ``(e1, e2)`` for each round.

    Returns
    -------
    List[str]
        Dialogue lines including state transitions and responses.
    """
    lines: List[str] = []
    for e1, e2 in updates:
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(e1)
        agent2.update_emotion(e2)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

