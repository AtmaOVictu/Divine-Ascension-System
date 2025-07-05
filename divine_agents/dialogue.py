from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # First emotional exchange
    agent1.update_emotion('jeza', 0.6)
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}")

    agent2.update_emotion('mir', 0.4)
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Resnica je?')}")

    # Second exchange may trigger state transitions
    agent1.update_emotion('radovednost', 0.3)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je zdaj resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je zdaj resnica?')}")
    return lines
