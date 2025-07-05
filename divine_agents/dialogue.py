from typing import List, Optional, Tuple
import random
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_pairs: Optional[List[Tuple[float, float]]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue with emotional influence."""
    lines: List[str] = []
    for idx in range(2):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        if emotion_pairs and idx < len(emotion_pairs):
            e1, e2 = emotion_pairs[idx]
        else:
            e1, e2 = random.uniform(0, 1), random.uniform(0, 1)
        agent1.update_emotion(e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        agent2.update_emotion(e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
