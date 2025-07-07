"""Dialogue utilities for ontological agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    for _ in range(2):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(agent1.emotion + 0.6)
        agent2.update_emotion(agent2.emotion + 0.4)

        agent1.transition()
        agent2.transition()

    lines.append(
        f"{agent1.name} končno stanje: {agent1.state}, emocija {agent1.emotion:.1f}"
    )
    lines.append(
        f"{agent2.name} končno stanje: {agent2.state}, emocija {agent2.emotion:.1f}"
    )
    return lines
