from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, topic: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements reflecting their current states.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")

    # Emotions rise due to disagreement, increasing tension.
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.8)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their new states.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")

    return lines
