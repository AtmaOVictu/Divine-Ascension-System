from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # First emotional reaction
    agent1.update_emotion('anger', 0.4)
    agent2.update_emotion('joy', 0.3)
    lines.append(f"{agent1.name}: {agent1.respond('Kako razumeš resnico?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako razumeš resnico?')}")

    # Intensify emotions leading to possible transitions
    agent1.update_emotion('anger', 0.5)
    agent2.update_emotion('joy', 0.5)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
