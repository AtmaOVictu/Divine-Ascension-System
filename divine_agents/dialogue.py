from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions influencing tension and possible transitions
    agent1.update_emotion(0.6, "jeza")
    agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.8, "strah")
    agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
