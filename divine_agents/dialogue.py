from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "fear")
    prev_state = agent1.state
    new_state = agent1.transition()
    if new_state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(0.6, "joy")
    prev_state = agent2.state
    new_state = agent2.transition()
    if new_state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
