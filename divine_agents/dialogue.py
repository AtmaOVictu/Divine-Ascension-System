"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a multi-step philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements about truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # First emotional reaction triggers possible transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico sedaj?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico sedaj?')}"
    )

    # Another round of emotions and potential transitions
    agent1.update_emotion(0.8, "joy")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "fear")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa koncna resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa koncna resnica?')}"
    )

    return lines
