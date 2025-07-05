from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical exchange between two agents."""

    lines: List[str] = []

    # Initial statements based on their current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional shift triggered by the dialogue
    agent1.set_emotion("anger", 0.6)
    agent1.regulate()
    agent1.modulate()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("joy", 0.8)
    agent2.regulate()
    agent2.modulate()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after emotional influence
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
