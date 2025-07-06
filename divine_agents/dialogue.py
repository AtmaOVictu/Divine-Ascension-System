"""Utilities to simulate philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where emotion influences state transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional responses influence transitions
    agent1.update_emotion(0.6, "jeza")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion(0.2, "veselje")
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_name} in prehaja v stanje: {agent2.transition()}"
    )

    # Follow-up reflection
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
