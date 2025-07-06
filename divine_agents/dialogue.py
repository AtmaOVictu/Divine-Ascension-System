"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise after first exchange
    agent1.update_emotion(0.4, 'anger')
    agent2.update_emotion(0.6, 'joy')

    # Perform potential transitions
    if agent1.tension > 0.7 or agent1.emotion > 0.5:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    if agent2.tension > 0.7 or agent2.emotion > 0.5:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
