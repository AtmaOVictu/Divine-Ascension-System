from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements based on their current ontological stances
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions to the discussion
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.4)
    agent2.update_tension(0.8)

    if agent1.can_transition():
        agent1.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    if agent2.can_transition():
        agent2.transition()
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Agents respond again from their (potentially) new perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
