from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           emotions: Iterable[tuple[float, str]] | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participants in the conversation.
    emotions:
        Optional sequence of ``(intensity, type)`` tuples applied sequentially
        to ``agent1`` and ``agent2``. If omitted, defaults are used.
    """

    if emotions is None:
        emotions = [(0.8, "anger"), (0.6, "joy")]

    lines: List[str] = []
    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")

    for idx, (e1, e2) in enumerate(zip(emotions[::2], emotions[1::2]), start=1):
        agent1.update_emotion(*e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(*e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")

    return lines
