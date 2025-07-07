from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} občuti napetost {agent1.tension:.1f} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} občuti napetost {agent2.tension:.1f} in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako razumeš resnico?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako razumeš resnico?')}"
    )
    return lines
