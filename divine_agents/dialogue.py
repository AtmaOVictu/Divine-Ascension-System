"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, question: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(agent1.philosophical_line(question))
    lines.append(agent2.philosophical_line(question))

    # apply emotional changes
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final statements after transitions
    lines.append(agent1.philosophical_line(question))
    lines.append(agent2.philosophical_line(question))

    return lines
