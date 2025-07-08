from typing import List
import random

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements reflecting ontological states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Incorporate new philosophical concepts
    concepts = ["absolutna resnica", "relativna resnica", "enotna resnica"]
    for concept in concepts:
        if agent1.process_knowledge(concept):
            lines.append(f"{agent1.name} razmišlja o {concept}.")
        if agent2.process_knowledge(concept):
            lines.append(f"{agent2.name} razmišlja o {concept}.")

    # Emotional impact leading to possible transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Random exploration to keep evolution dynamic
    if random.random() < 0.3:
        item = agent1.knowledge_base.random_explore()
        if item:
            lines.append(f"{agent1.name} naključno razmišlja o: {item}")

    if random.random() < 0.3:
        item = agent2.knowledge_base.random_explore()
        if item:
            lines.append(f"{agent2.name} naključno razmišlja o: {item}")

    # Closing answers influenced by new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
