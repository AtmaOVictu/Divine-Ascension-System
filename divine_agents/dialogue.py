from typing import List

from .agent import Agent
from .advanced import MultiLayerDecisionMaker, ExperienceBasedLearning


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    decision1 = MultiLayerDecisionMaker(agent1).multi_layer_decision()
    lines.append(f"{agent1.name} prehaja v stanje: {decision1}")

    agent2.update_emotion(0.6)
    agent2.add_experience("selfish")
    decision2 = MultiLayerDecisionMaker(agent2).multi_layer_decision()
    lines.append(f"{agent2.name} prehaja v stanje: {decision2}")

    learning1 = ExperienceBasedLearning(agent1).learn_from_experience("danger")
    lines.append(f"{agent1.name} se odziva: {learning1}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
