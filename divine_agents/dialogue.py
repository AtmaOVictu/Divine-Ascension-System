from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Tuple[Tuple[str, float], Tuple[str, float]] = (("fear", 0.8), ("joy", 0.6)),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.experience_emotion(*emotions[0])
    lines.append(
        f"{agent1.name} čuti {emotions[0][0]} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.experience_emotion(*emotions[1])
    lines.append(
        f"{agent2.name} čuti {emotions[1][0]} in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
