from typing import List
from .agent import Agent, VersionedAgent


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


def interactive_contact_dialogue(agent1: VersionedAgent, agent2: VersionedAgent) -> List[str]:
    """Dialogue where agents interact via contact triggering version changes."""
    lines = []
    lines.append(f"{agent1.name} verzija {agent1.version}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} verzija {agent2.version}: {agent2.respond('Kaj je resnica?')}")

    agent1.contact(agent2)
    lines.append(f"{agent1.name} prehaja v {agent1.state}, verzija {agent1.version}")

    agent2.contact(agent1)
    lines.append(f"{agent2.name} prehaja v {agent2.state}, verzija {agent2.version}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
