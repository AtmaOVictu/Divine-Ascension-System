from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
    mood1: str = "joy",
    mood2: str = "anger",
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion1, mood1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2, mood2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
