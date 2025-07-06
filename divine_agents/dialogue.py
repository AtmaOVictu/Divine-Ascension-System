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

    agent1.express_emotion("anger")
    prev = agent1.state
    agent1.transition()
    if prev != agent1.state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.express_emotion("fear")
    prev = agent2.state
    agent2.transition()
    if prev != agent2.state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
