"""Utilities for simulating philosophical dialogue between ontological agents."""
from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a brief dialogue where agents may change states based on emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to each other's views
    agent1.update_emotion('anger', 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion('joy', 0.7)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of statements after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
