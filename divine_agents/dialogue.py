from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, emo1: float, emo2: float) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotions provided influence tension and may trigger state transitions.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emo1)
    transition1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {transition1}")

    agent2.update_emotion(emo2)
    transition2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {transition2}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
