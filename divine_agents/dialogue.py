from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Opening statements reflecting current state
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions to the initial exchange
    agent1.update_emotion(0.6, "anger")
    if agent1.transition() != agent1.history[-2]:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.8, "joy")
    if agent2.transition() != agent2.history[-2]:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Responses after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako to razložite?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako to razložite?')}"
    )

    return lines
