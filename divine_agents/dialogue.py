from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    agent1_emotion: Tuple[str, float] = ("joy", 0.8),
    agent2_emotion: Tuple[str, float] = ("anger", 0.6),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): {agent1.respond('Kaj je resnica?')}"
    )
    agent1.update_emotion(*agent1_emotion)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): {agent2.respond('Kaj je resnica?')}"
    )
    agent2.update_emotion(*agent2_emotion)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
