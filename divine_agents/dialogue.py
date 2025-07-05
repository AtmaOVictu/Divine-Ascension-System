from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
        agent1.experience_emotion(0.3)
        prev = agent1.state
        agent1.transition()
        if agent1.state != prev:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")
        agent2.experience_emotion(0.4)
        prev = agent2.state
        agent2.transition()
        if agent2.state != prev:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
