"""Conversation utilities for ontological agents."""

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

    # Emotional reaction and potential transition after hearing the other agent
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of conversation influenced by new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('In kaj pa ti mislis?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Resnica se razvija.')}"
    )

    return lines
