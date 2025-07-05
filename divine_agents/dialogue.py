from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions grow as the debate continues
    agent1.update_emotion(0.4, "anger")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako lahko misliš drugače?')}")

    agent2.update_emotion(0.2, "joy")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Resnica je lahko različna.')}")

    # Escalation causing transitions
    agent1.update_emotion(0.5, "fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections from new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica sedaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako razumeš resnico sedaj?')}")

    return lines
