from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # Initial statements reflecting current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise as debate unfolds
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.75)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of statements after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako sedaj vidiš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako sedaj vidiš resnico?')}")

    return lines
