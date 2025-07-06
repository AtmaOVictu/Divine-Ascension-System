from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions to drive transitions
        agent1.update_emotion(min(1.0, agent1.emotion + 0.4), emotion_type="anger")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(1.0, agent2.emotion + 0.3), emotion_type="joy")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines

