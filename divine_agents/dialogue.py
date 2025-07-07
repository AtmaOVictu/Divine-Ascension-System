"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial responses based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the debate
    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Reach the peak of tension and reset via unity
    agent1.update_tension(1.0)
    lines.append(f"{agent1.name} dosega: {agent1.history[-2]}")

    agent2.update_emotion("sorrow", 1.0)
    lines.append(f"{agent2.name} dosega: {agent2.history[-2]}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
