from typing import List

from .agent import Agent
from .emotion import Emotion
from .karma import Karma
from .network import AgentNetwork


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    network = AgentNetwork(2)
    network.update_emotions([[0.0, 1.0], [1.0, 0.0]])

    agent1.update_emotion(0.8)
    network.emotions[0] = agent1.emotion
    agent2.update_emotion(0.6)
    network.emotions[1] = agent2.emotion

    agent1.transition()
    agent2.transition()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
