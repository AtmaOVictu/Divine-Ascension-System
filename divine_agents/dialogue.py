from typing import List

from .agent import Agent
from .ontology import OntologicalDictionary
from .writing import WritingAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    dictionary = OntologicalDictionary()
    writer1 = WritingAgent(agent1.name)
    writer2 = WritingAgent(agent2.name)

    lines: List[str] = []

    resp1 = agent1.respond("Kaj je resnica?")
    lines.append(f"{agent1.name} ({agent1.state}): {resp1}")
    writer1.write_event("dialogue", agent1.state, resp1)

    resp2 = agent2.respond("Kaj je resnica?")
    lines.append(f"{agent2.name} ({agent2.state}): {resp2}")
    writer2.write_event("dialogue", agent2.state, resp2)

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    writer1.write_event("transition", agent1.state, agent1.respond("Kaj je resnica?"))

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    writer2.write_event("transition", agent2.state, agent2.respond("Kaj je resnica?"))

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    meaning = dictionary.get_word_meaning("truth")
    lines.append(f"Ontološki pomen 'resnica': {meaning['philosophical_meaning']}")

    return lines
