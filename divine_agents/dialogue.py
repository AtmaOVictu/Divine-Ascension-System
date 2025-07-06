from typing import List

from .agent import Agent
from .opposites import OntologicalOppositesGenerator


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


def dialogue_with_opposites(
    agent1: Agent, agent2: Agent, generator: OntologicalOppositesGenerator
) -> List[str]:
    """Dialogue that also introduces a random pair of opposites."""
    lines = philosophical_dialogue(agent1, agent2)
    pair = generator.generate_opposites()
    lines.append(f"Nasprotje: {pair[0]} ↔ {pair[1]}")
    lines.append(generator.create_transition(pair[0]))
    return lines
