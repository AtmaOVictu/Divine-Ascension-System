from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 2) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(steps):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.adjust_emotion(0.4)
        prev1 = agent1.state
        agent1.transition()
        if agent1.state != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.adjust_emotion(0.4)
        prev2 = agent2.state
        agent2.transition()
        if agent2.state != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    return lines
