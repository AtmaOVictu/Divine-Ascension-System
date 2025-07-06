from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current state
    lines.append(
        f"{agent1.name} ({agent1.symbol()}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.symbol()}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during conversation
    agent1.update_emotion(0.8, "jeza")
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} {agent1.symbol()}"
    )

    agent2.update_emotion(0.6, "veselje")
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} {agent2.symbol()}"
    )

    # Agents respond again with new states and emotions
    lines.append(
        f"{agent1.name} ({agent1.symbol()}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.symbol()}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
