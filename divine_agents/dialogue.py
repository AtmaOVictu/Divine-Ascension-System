from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical exchange influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions arise during the debate
    agent1.apply_emotion('anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion('joy')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after emotional shift
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
