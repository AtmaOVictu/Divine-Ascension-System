from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Tuple[Tuple[str, float], Tuple[str, float]] = (("fear", 0.8), ("joy", 0.6)),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents engaged in dialogue.
    emotions:
        Tuples of emotion label and intensity for agent1 and agent2 respectively.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    label1, intensity1 = emotions[0]
    agent1.update_emotion(intensity1, label1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    label2, intensity2 = emotions[1]
    agent2.update_emotion(intensity2, label2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
