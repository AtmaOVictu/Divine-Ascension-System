from typing import List

from .agent import Agent
from .reason import LogarithmOfReason


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue between two agents with emotions."""
    lines: List[str] = []
    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Intensify emotions leading to possible transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Present reasoning behind transitions
    reason1 = LogarithmOfReason(agent1).calculate()
    reason2 = LogarithmOfReason(agent2).calculate()
    lines.append(f"{agent1.name}: {reason1}")
    lines.append(f"{agent2.name}: {reason2}")

    # Final responses from new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
