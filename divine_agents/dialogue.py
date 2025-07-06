from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def debate_truth(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate debate on absolute vs relative truth and induce transitions."""
    lines = []
    # Initial statements based on their current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Heighten emotions/tension through debate
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako zdaj vidiš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako zdaj vidiš resnico?')}")
    return lines
