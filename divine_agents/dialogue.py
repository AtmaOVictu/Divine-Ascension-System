"""Simple dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('resnica')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('resnica')}")

    # Emotions rise due to arguments
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('resnica')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('resnica')}")

    return lines
