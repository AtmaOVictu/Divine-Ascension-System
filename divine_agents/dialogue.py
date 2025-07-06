from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, iterations: int = 2) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    emotion_cycle = [("anger", 0.4), ("fear", 0.4), ("joy", 0.3)]

    for i in range(iterations):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        e1, v1 = emotion_cycle[i % len(emotion_cycle)]
        e2, v2 = emotion_cycle[(i + 1) % len(emotion_cycle)]
        agent1.update_emotion(e1, v1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(e2, v2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
