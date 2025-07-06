from typing import List
from .agent import Agent, DynamicAgent
from .dynamics import EmotionalTensionDynamics


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


def advanced_dialogue(agent1: DynamicAgent, agent2: DynamicAgent) -> List[str]:
    """Conduct a dialogue using dynamic agents with emotion-driven transitions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    dyn1 = EmotionalTensionDynamics(agent1)
    dyn2 = EmotionalTensionDynamics(agent2)
    dyn1.adjust_tension()
    dyn2.adjust_tension()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.multi_layer_transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.multi_layer_transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
