"""Dialogue utilities for philosophical debates between agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    old_state = agent1.state
    agent1.transition()
    if agent1.state != old_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    old_state = agent2.state
    agent2.transition()
    if agent2.state != old_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Extended dialogue demonstrating emotional influence and transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise after hearing the other's view
    old_state1 = agent1.state
    agent1.update_emotion(0.6)
    agent1.transition()
    if agent1.state != old_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    old_state2 = agent2.state
    agent2.update_emotion(0.7)
    agent2.transition()
    if agent2.state != old_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final responses based on new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
