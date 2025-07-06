from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate between two agents.

    Agent1 starts from the Ego perspective while Agent2 starts from Jaz.
    Each round emotions intensify, possibly triggering state transitions.
    """
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents feel emotions after hearing each other
    agent1.feel('anger', 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.feel('joy', 0.4)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Additional emotional escalation to potentially reach Enotnost
    agent1.feel('curiosity', 0.3)
    agent2.feel('inspiration', 0.6)
    lines.append(f"{agent2.name} ponovno prehaja v stanje: {agent2.transition()}")

    # Second round of dialogue after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
