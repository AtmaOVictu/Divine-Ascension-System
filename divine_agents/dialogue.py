from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           emo1: float = 0.8, emo2: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotional intensities ``emo1`` and ``emo2`` are applied to ``agent1`` and
    ``agent2`` respectively, potentially causing state transitions.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emo1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emo2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
