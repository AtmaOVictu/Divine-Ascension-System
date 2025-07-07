from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical debate influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents experience emotions influencing tension
    agent1.update_emotion("fear", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after emotional change
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
