from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # apply nano events to both agents
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.nano_event(0.8, 0.8)}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.nano_event(0.6, 0.6)}")

    # possible mega transition if tension rises high
    agent1.update_tension(1.2)
    lines.append(f"{agent1.name} MEGA prehod: {agent1.mega_transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
