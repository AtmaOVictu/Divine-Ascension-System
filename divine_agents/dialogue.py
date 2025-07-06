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

    # Agent1 reacts with anger causing a transition
    agent1.update_emotion("jeza", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )

    # Agent2 feels joy and may also transition
    agent2.update_emotion("veselje", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
