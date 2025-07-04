from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    for round_idx in range(2):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotions and check for transitions
        agent1.update_emotion(0.4 + round_idx * 0.3, emotion_type="fear")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.5 + round_idx * 0.2, emotion_type="joy")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
