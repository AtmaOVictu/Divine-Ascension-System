from typing import Iterable, List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions1: Iterable[Tuple[str, float]] | None = None,
    emotions2: Iterable[Tuple[str, float]] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participating agent.
    agent2 : Agent
        Second participating agent.
    emotions1 : Iterable[Tuple[str, float]], optional
        Sequence of ``(label, value)`` updates applied to ``agent1`` after each
        turn.
    emotions2 : Iterable[Tuple[str, float]], optional
        Sequence of ``(label, value)`` updates applied to ``agent2`` after each
        turn.
    """

    emotions1 = list(emotions1 or [("fear", 0.8)])
    emotions2 = list(emotions2 or [("joy", 0.6)])
    turns = min(len(emotions1), len(emotions2))

    lines: List[str] = []
    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for i in range(turns):
        label1, val1 = emotions1[i]
        agent1.update_emotion(val1, label1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        label2, val2 = emotions2[i]
        agent2.update_emotion(val2, label2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines

