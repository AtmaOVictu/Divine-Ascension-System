from typing import List
from .agent import Agent, MultiLayerTransitionSystem


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def advanced_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate dialogue with emotional dynamics and multi-layer transitions."""
    ml1 = MultiLayerTransitionSystem(agent1)
    ml2 = MultiLayerTransitionSystem(agent2)

    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotional_state("fearful")
    lines.append(f"{agent1.name} prehaja v stanje: {ml1.multi_layer_transition()}")

    agent2.set_emotional_state("happy")
    agent2.loyalty = 0.9
    lines.append(f"{agent2.name} prehaja v stanje: {ml2.multi_layer_transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
