"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue illustrating different views on truth."""

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    # Increase emotions which may trigger transitions
    agent1.update_emotion("anger", 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    return lines
