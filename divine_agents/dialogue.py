from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, cycles: int = 2) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    for i in range(cycles):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        if i == 0:
            agent1.update_emotion("jeza", 0.4)
            agent2.update_emotion("veselje", 0.3)
        else:
            agent1.update_emotion("radovednost", 0.4)
            agent2.update_emotion("spokojnost", 0.4)

        agent1.transition()
        agent2.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    return lines
