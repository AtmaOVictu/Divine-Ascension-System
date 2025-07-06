"""Dialogue helpers for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements reflecting current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reaction after hearing the other's statement
    agent1.update_emotion(0.6)
    lines.append(
        f"{agent1.name} čuti napetost {agent1.tension:.2f} in prehaja v: {agent1.transition()}"
    )

    agent2.update_emotion(0.8)
    lines.append(
        f"{agent2.name} čuti napetost {agent2.tension:.2f} in prehaja v: {agent2.transition()}"
    )

    # Final responses from their new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
