from typing import List
from .agent import Agent


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

from .dictionary import OntologicalDictionary
from .writer import WritingAgent


def philosophical_dialogue_with_writer(
    agent1: Agent, agent2: Agent, writer: WritingAgent, dictionary: OntologicalDictionary
) -> List[str]:
    """Simulate dialogue and record transitions using the writer."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    writer.write_event("start", agent1.state + '/' + agent2.state, "Beginning of dialogue")

    fear = dictionary.get_word_meaning("fear")
    agent1.update_emotion(fear["emotional_intensity"])
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    writer.write_event("agent1 transition", agent1.state, "Fear triggered")

    joy = dictionary.get_word_meaning("joy")
    agent2.update_emotion(joy["emotional_intensity"])
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    writer.write_event("agent2 transition", agent2.state, "Joy triggered")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    writer.write_event("end", agent1.state + '/' + agent2.state, "Dialogue finished")
    return lines
