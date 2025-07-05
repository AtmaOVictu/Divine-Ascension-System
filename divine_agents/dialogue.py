from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional responses influence tension and possible transitions
    agent1.update_emotion(0.6, "anger")
    previous = agent1.state
    agent1.transition()
    if agent1.state != previous:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6, "joy")
    previous = agent2.state
    agent2.transition()
    if agent2.state != previous:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Responses after experiencing emotions and potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico sedaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico sedaj?')}")

    return lines
