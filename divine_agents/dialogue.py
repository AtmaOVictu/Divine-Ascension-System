from typing import List
from .agent import Agent, VersionedAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if isinstance(agent1, VersionedAgent):
        agent1.touch(agent2)
        lines.append(f"{agent1.name} prehaja v {agent1.version} in stanje: {agent1.state}")
    else:
        agent1.update_emotion(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    if isinstance(agent2, VersionedAgent):
        agent2.touch(agent1)
        lines.append(f"{agent2.name} prehaja v {agent2.version} in stanje: {agent2.state}")
    else:
        agent2.update_emotion(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
