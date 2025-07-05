"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical exchange between two agents."""

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to the arguments
    agent1.update_emotion(0.6, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "sreča")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of answers from the new states
    lines.append(f"{agent1.name} ({agent1.emotion.name}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.emotion.name}): {agent2.respond('Kaj je resnica?')}")

    return lines
