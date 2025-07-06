from typing import List, Optional
from .agent import Agent
from .archive import Archive, Contact


def philosophical_dialogue(agent1: Agent, agent2: Agent, archive: Optional[Archive] = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    If an archive is provided, all interactions will be stored as contacts.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if archive is not None:
        archive.add_contact(Contact(agent1.name, agent2.name, 'start', 0))

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    if archive is not None:
        archive.add_contact(Contact(agent1.name, agent2.name, 'after_transition', 1))

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
