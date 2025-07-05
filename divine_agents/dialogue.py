from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial views
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions arise after hearing the other's view
    agent1.update_emotion(0.6, 'anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")

    agent2.update_emotion(0.4, 'joy')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Further discussion creates more tension
    agent1.update_emotion(0.3, 'sorrow')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")

    agent2.update_emotion(0.5, 'empathy')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
