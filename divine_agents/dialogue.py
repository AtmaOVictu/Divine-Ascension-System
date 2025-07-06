from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""

    lines: List[str] = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        if i == 0:
            agent1.update_emotion(0.6, "anger")
            agent2.update_emotion(0.6, "fear")
        else:
            agent1.update_emotion(min(agent1.emotion + 0.3, 1.0), "joy")
            agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), "joy")

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
