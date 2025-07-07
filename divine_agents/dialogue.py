"""Dialogue utilities for ontological agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Both agents start by expressing their view on truth. Emotions are then
    updated which may trigger state transitions. The resulting statements
    reflect the new ontological and emotional states.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions
    old_state = agent1.state
    agent1.update_emotion(0.6, "jeza")
    agent1.transition()
    if agent1.state != old_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    old_state = agent2.state
    agent2.update_emotion(0.6, "veselje")
    agent2.transition()
    if agent2.state != old_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
