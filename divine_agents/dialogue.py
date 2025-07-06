from typing import List, Optional
from .agent import Agent
from .archive import Archive, Contact


def philosophical_dialogue(agent1: Agent, agent2: Agent, archive: Optional[Archive] = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    If an ``Archive`` is provided, all exchanges are stored as ``Contact`` entries.
    """
    lines: List[str] = []

    def record(speaker: Agent, listener: Agent, text: str) -> None:
        if archive is not None:
            archive.add_contact(Contact(speaker.name, listener.name, text, str(len(archive.contacts))))

    opening1 = agent1.respond("Kaj je resnica?")
    lines.append(f"{agent1.name} ({agent1.state}): {opening1}")
    record(agent1, agent2, opening1)

    opening2 = agent2.respond("Kaj je resnica?")
    lines.append(f"{agent2.name} ({agent2.state}): {opening2}")
    record(agent2, agent1, opening2)

    agent1.update_emotion(0.8)
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

    agent2.update_emotion(0.6)
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    response1 = agent1.respond("Kaj je resnica?")
    lines.append(f"{agent1.name}: {response1}")
    record(agent1, agent2, response1)

    response2 = agent2.respond("Kaj je resnica?")
    lines.append(f"{agent2.name}: {response2}")
    record(agent2, agent1, response2)

    return lines
