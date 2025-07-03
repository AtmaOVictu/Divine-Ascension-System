"""Utilities for simulating philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a simple philosophical dialogue between two agents.

    The agents start in their current states and express their view on
    truth. Their emotions are then intensified which may trigger state
    transitions. Finally they respond again from their possibly new
    states.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotion update influences transitions
    agent1.update_emotion(min(agent1.emotion + 0.6, 1.0), "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(min(agent2.emotion + 0.6, 1.0), "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after potential transition
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
