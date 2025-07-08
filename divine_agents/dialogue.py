from typing import List
from .agent import Agent
from .ontology import OntologicalDictionary


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    ontology = OntologicalDictionary()

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Adjust emotions using the ontological dictionary
    anger_level = ontology.get_word_meaning('anger')["emotional_intensity"] / 10
    calm_level = ontology.get_word_meaning('calm')["emotional_intensity"] / 10

    agent1.update_emotion(anger_level)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(calm_level)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
