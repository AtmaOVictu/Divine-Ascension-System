"""Utility helpers for running short philosophical dialogues."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Each agent responds based on its ontological state. After the initial
    exchange their emotions increase which may lead to a state transition.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Debate causes emotional reactions
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # Perform possible transitions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses reflect new states and emotions
    lines.append(f"{agent1.name}: {agent1.respond('Kako vidiš resnico sedaj?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako vidiš resnico sedaj?')}")

    return lines
