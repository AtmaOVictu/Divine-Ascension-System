from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")

        agent1.adjust_emotion(0.6)
        agent2.adjust_emotion(0.6)

        prev1, prev2 = agent1.state, agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
