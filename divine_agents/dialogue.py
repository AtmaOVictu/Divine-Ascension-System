"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions during conversation
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.8)

    prev_state1 = agent1.state
    prev_state2 = agent2.state

    if agent1.transition() != prev_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.transition() != prev_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
