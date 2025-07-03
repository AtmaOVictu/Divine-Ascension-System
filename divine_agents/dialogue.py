from typing import List, Tuple
from .agent import Agent


EmotionSpec = Tuple[str, float]


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: EmotionSpec,
    emotion2: EmotionSpec,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.apply_emotion(*emotion1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion(*emotion2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
