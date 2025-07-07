from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function demonstrates how emotional intensity and type influence
    the philosophical conversation and resulting state transitions.
    """
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during debate, affecting tension and potential transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their possibly new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Ali je resnica absolutna?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Ali je resnica relativna?')}"
    )

    return lines
