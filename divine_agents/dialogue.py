from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    agent1.update_fame(3, 1, 5)
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} (fame: {agent1.fame})"
    )

    agent2.update_emotion(0.6)
    agent2.update_fame(1, 0, 2)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} (fame: {agent2.fame})"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
