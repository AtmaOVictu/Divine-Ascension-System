from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise after the first exchange
    agent1.update_emotion(0.6, 'jeza')
    agent2.update_emotion(0.6, 'veselje')

    # State transitions triggered by new emotions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange reflects new states and emotions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico sedaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico sedaj?')}")

    return lines
