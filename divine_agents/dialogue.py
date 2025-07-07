from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions triggered by the conversation
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.8)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # New responses after emotional change
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico?')}"
    )
    return lines
