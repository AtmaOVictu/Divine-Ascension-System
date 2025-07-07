"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent, State


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('')}")

    # emotions rise through the exchange
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    # final responses
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('')}")
    return lines
