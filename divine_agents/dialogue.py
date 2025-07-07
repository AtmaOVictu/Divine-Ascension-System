from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    q = "Kaj je resnica?"
    first = agent1.respond(q)
    lines.append(f"{agent1.name} ({agent1.state}): {first}")

    second = agent2.respond(q)
    lines.append(f"{agent2.name} ({agent2.state}): {second}")

    # Agents react to the previous statement by updating emotions and possibly transitioning
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    reaction1 = agent1.respond(second)
    lines.append(f"{agent1.name} ({agent1.state}): {reaction1}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    reaction2 = agent2.respond(reaction1)
    lines.append(f"{agent2.name} ({agent2.state}): {reaction2}")

    return lines
