from typing import List
from .agent import Agent
from .dictionary import OntologicalDictionary
from .writer import WritingAgent


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


def reflective_dialogue(
    agent1: Agent, agent2: Agent, dictionary: OntologicalDictionary, writer: WritingAgent
) -> List[str]:
    """Simulate dialogue while recording events with emotional context."""
    lines: List[str] = []

    line = f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    lines.append(line)
    writer.write_event("initial", agent1.state, line, agent1.emotion)

    line = f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    lines.append(line)
    writer.write_event("initial", agent2.state, line, agent2.emotion)

    agent1.update_from_emotion_word("anger", dictionary)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    writer.write_event("transition", agent1.state, "based on anger", agent1.emotion)

    agent2.update_from_emotion_word("fear", dictionary)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    writer.write_event("transition", agent2.state, "based on fear", agent2.emotion)

    line = f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    lines.append(line)
    writer.write_event("final", agent1.state, line, agent1.emotion)

    line = f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    lines.append(line)
    writer.write_event("final", agent2.state, line, agent2.emotion)

    return lines
