"""Dialogue utilities for philosophical conversations."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation demonstrates how emotions influence state transitions.
    """
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions affect tension and may lead to transitions
    agent1.update_emotion('anger', 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion('joy', 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico?')}")

    return lines
