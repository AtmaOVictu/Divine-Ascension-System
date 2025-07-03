from typing import List, Tuple
from .agent import Agent

Emotion = Tuple[str, float]


def philosophical_debate(agent1: Agent, agent2: Agent, emotion1: Emotion, emotion2: Emotion) -> List[str]:
    """Simulate a dialogue that updates emotions and transitions."""
    lines: List[str] = []
    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # apply emotions
    agent1.update_emotion(emotion1[1], emotion1[0])
    agent2.update_emotion(emotion2[1], emotion2[0])
    lines.append(f"{agent1.name} \u010duti {emotion1[0]} in prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} \u010duti {emotion2[0]} in prehaja v stanje: {agent2.transition()}")

    # second round of statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
