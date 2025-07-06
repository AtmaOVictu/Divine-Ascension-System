from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements using phonetic triggers
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('ba')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('ka')}")

    # Update emotional state which may trigger transitions
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Additional tension to allow further transition for agent2
    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond()}")
    lines.append(f"{agent2.name}: {agent2.respond()}")
    return lines
