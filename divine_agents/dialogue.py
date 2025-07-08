"""Utilities for creating philosophical dialogues between agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Return a scripted interaction between two agents.

    Each participant initially answers a question about truth from the
    perspective of their current ontological state. Emotional intensity is
    then increased to trigger potential state transitions, after which the
    agents respond again.
    """

    lines = []  # Collect dialogue lines in order
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Heighten emotions to encourage state transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Respond again after potential state changes
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

