"""Utility functions for running philosophical dialogues between agents."""

from typing import Iterable, List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           emotions: Iterable[tuple[float, float]] = ((0.8, 0.6),)) -> List[str]:
    """Simulate a philosophical dialogue.

    Parameters
    ----------
    agent1, agent2:
        Conversing agents.
    emotions:
        Iterable of emotion tuples ``(e1, e2)`` applied at each step.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for e1, e2 in emotions:
        agent1.update_emotion(e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
