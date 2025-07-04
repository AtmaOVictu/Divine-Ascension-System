"""Dialogue helpers for philosophical exchanges between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a brief philosophical exchange between two agents."""

    lines: List[str] = []
    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions escalate as discussion unfolds
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)
    agent1.transition()
    agent2.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Agents respond again from their possibly new perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa zdaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa zdaj?')}")

    return lines
