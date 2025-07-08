from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")

    # First emotional exchange
    agent1.update_emotion(0.8, "jezo")
    agent2.update_emotion(0.6, "veselje")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange potentially leading to higher state
    agent2.update_emotion(0.8, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")
    return lines
