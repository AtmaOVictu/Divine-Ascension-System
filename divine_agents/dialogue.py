from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue with emotion-driven transitions."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        if agent1.state != agent2.state:
            agent1.update_emotion(min(agent1.emotion + 0.3, 1.0), "anger")
            agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), "fear")
        else:
            agent1.update_emotion(max(agent1.emotion - 0.1, 0.0))
            agent2.update_emotion(max(agent2.emotion - 0.1, 0.0))

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
