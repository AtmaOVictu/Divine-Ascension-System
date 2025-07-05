from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during discussion
    agent1.update_emotion("anger", 0.8)
    agent2.update_emotion("joy", 0.6)

    # State transitions if thresholds exceeded
    prev1 = agent1.state
    prev2 = agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
