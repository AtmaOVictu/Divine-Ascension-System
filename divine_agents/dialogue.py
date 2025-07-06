"""Utility for simulating philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial exchange about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the discussion
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # Perform possible state transitions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of discussion with potential new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa relativna resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa absolutna resnica?')}")

    return lines
