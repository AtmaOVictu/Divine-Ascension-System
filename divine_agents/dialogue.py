from typing import List

from .agent import Agent
from .transition import MultiLayerTransitionSystem


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a simple dialogue between two agents with emotional influence."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.6)
    MultiLayerTransitionSystem(agent1).multi_layer_transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.8)
    MultiLayerTransitionSystem(agent2).multi_layer_transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
