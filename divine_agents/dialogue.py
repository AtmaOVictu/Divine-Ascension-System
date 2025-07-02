from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Opening statements based on current states.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Dialogue influences emotions which in turn may trigger transitions.
    agent1.update_emotion(0.6, "anger")
    agent2.update_emotion(0.6, "joy")

    before = agent1.state
    after = agent1.transition()
    if before != after:
        lines.append(f"{agent1.name} prehaja v stanje: {after}")

    before = agent2.state
    after = agent2.transition()
    if before != after:
        lines.append(f"{agent2.name} prehaja v stanje: {after}")

    # Closing statements after potential transitions.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
