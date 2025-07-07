from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Opening statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # First emotional reaction triggers a potential transition for agent1
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")

    # Agent2 reacts calmly and stays in its state
    agent2.update_emotion(0.4, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Tension rises further, leading to additional transitions
    agent2.update_emotion(0.8, "fear")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.5, "sorrow")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")

    return lines
