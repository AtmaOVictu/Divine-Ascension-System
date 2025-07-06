from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    # Intensify emotions and trigger transitions if thresholds are met
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange reflects new states and emotions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    return lines
