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

    # Agent1 reagira z jezo na relativni pogled resnice
    agent1.apply_emotion("anger", 0.6)
    lines.append(
        f"{agent1.name} čuti jezo in prehaja v stanje: {agent1.transition()}"
    )

    # Agent2 ostaja miren, a nekoliko vesel zaradi odziva
    agent2.apply_emotion("joy", 0.4)
    lines.append(
        f"{agent2.name} izraža veselje in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
