from typing import List
from .agent import Agent
from .coincidence import happy_coincidence


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # A happy coincidence influences both agents
    event, s1, s2 = happy_coincidence(agent1, agent2)
    lines.append(f"Dogodek: {event}")
    lines.append(f"{agent1.name} prehaja v stanje: {s1}")
    lines.append(f"{agent2.name} prehaja v stanje: {s2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
