"""Utilities for simulating philosophical dialogues between agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a brief dialogue and trigger state transitions."""

    lines: List[str] = []

    # Initial exchange based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the debate
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Respond again from the new ontological perspective
    lines.append(f"{agent1.name}: {agent1.respond('Kaj pa sedaj?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj pa sedaj?')}")
    return lines
