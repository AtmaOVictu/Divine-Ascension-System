from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reaction from both agents leading to potential transitions
    agent1.update_emotion(0.8)
    agent1_state = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1_state}")

    agent2.update_emotion(0.6)
    agent2_state = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2_state}")

    # Responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
