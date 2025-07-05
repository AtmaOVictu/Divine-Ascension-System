"""Dialogue utilities between agents."""
from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""

    lines: List[str] = []
    # Initial stances
    lines.append(agent1.speak())
    lines.append(agent2.speak())

    # Emotions rise during debate
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final stances after emotional influence
    lines.append(agent1.speak())
    lines.append(agent2.speak())
    return lines
