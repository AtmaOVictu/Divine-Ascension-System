from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions to the initial exchange
    agent1.update_emotion("jeza", 0.4)
    lines.append(f"{agent1.name} čuti jezo.")
    agent2.update_emotion("prepričanost", 0.3)
    lines.append(f"{agent2.name} čuti prepričanost.")

    # Responses after emotions change
    lines.append(f"{agent1.name}: {agent1.respond('Kako razumeš resnico?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako razumeš resnico?')}")

    # Further emotional escalation leading to potential transitions
    agent1.update_emotion("strah", 0.5)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    agent2.update_emotion("veselje", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
