from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions
    agent1.update_emotion(0.6, "anger")
    new_state_1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state_1}")

    agent2.update_emotion(0.7, "sorrow")
    new_state_2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state_2}")

    # Second round after transition
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
