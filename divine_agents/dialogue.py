"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    # update emotions based on the first round
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # transitions may occur
    old_state1 = agent1.state
    old_state2 = agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != old_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != old_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # second exchange after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    return lines
