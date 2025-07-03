"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where emotions drive state transitions."""
    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional escalation
    agent1.set_emotion("jeza", 0.8)
    lines.append(f"{agent1.name} čuti {agent1.emotion_name}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("strah", 0.6)
    lines.append(f"{agent2.name} čuti {agent2.emotion_name}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # New philosophical positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
