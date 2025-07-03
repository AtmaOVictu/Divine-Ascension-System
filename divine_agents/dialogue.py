"""Utilities to simulate philosophical dialogue between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents update their emotional states during the conversation which may
    trigger state transitions.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    # Dialogue triggers emotional responses
    agent1.update_emotion("jeza", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("veselje", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    return lines
