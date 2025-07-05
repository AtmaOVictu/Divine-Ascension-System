from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, cycles: int = 3) -> List[str]:
    """Simulate a philosophical dialogue between two agents over several cycles."""
    lines: List[str] = []

    for _ in range(cycles):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.feel("jeza", 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.feel("radovednost", 0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
