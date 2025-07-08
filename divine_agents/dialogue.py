from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where tension and emotions trigger transitions."""
    lines: List[str] = []

    # Initial views on truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Arguments raise emotions and tension
    agent1.update_emotion("anger", 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako razumes resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako razumes resnico?')}")
    return lines
