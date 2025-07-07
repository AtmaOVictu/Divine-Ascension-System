from typing import List

from .agent import Agent
from .emotion import Emotion


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts angrily to Agent2's argument and may transition
    agent1.update_emotion(Emotion.ANGER, 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 gains confidence and joy in response
    agent2.update_emotion(Emotion.JOY, 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
