from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate influenced by emotions."""
    lines = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.4, 'anger')
    lines.append(f"{agent1.name} ({agent1.emotion_type}): {agent1.respond('Ne strinjam se!')}")

    agent2.update_emotion(0.3, 'joy')
    lines.append(f"{agent2.name} ({agent2.emotion_type}): {agent2.respond('Resnica je lahko večplastna.')}")

    agent1.update_emotion(0.4, 'fear')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Morda imaš prav.')}")

    agent2.update_emotion(0.6, 'joy')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Skupaj najdimo resnico.')}")

    return lines
