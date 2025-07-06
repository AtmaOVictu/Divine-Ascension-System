"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""

    lines: List[str] = []

    # Initial exchange
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions altering tension
    agent1.update_emotion(0.6, "jeza")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion(0.7, "veselje")
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_name} in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
