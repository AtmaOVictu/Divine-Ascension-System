"""Utilities for simulating philosophical conversations."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(agent1.talk("Kaj je resnica?"))
    lines.append(agent2.talk("Kaj je resnica?"))

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(agent1.talk("Kaj je resnica?"))
    lines.append(agent2.talk("Kaj je resnica?"))
    return lines
