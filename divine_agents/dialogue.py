from typing import List
from .agent import Agent
from .dictionary import OntologicalDictionary


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    dictionary = OntologicalDictionary()
    lines: List[str] = []

    # Opening statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Trigger emotion 'anger' for agent1
    anger = dictionary.get_word_meaning('anger')
    agent1.update_emotion(anger['emotional_intensity'])
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 experiences 'truth' then 'anger' leading to higher tension
    truth = dictionary.get_word_meaning('truth')
    agent2.update_emotion(truth['emotional_intensity'])
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    agent2.update_emotion(anger['emotional_intensity'])
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
