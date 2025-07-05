"""Conversation helpers for ontological agents."""

from typing import List

from .agent import Agent, State


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements based on current states
    lines.append(agent1.respond("Kaj je resnica?"))
    lines.append(agent2.respond("Kaj je resnica?"))

    # Emotional change influences tension and possible transitions
    agent1.update_emotion(0.8, emotion="fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")

    agent2.update_emotion(0.6, emotion="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    # Responses after potential state changes
    lines.append(agent1.respond("Kaj je resnica?"))
    lines.append(agent2.respond("Kaj je resnica?"))

    return lines
