from typing import List

from .agent import Agent
from .reason import LogarithmOfReason


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


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Extended debate where emotions influence transitions and reasoning."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.8)

    # Reasons and transitions
    reason1 = LogarithmOfReason(agent1).calculate_reason()
    lines.append(f"{agent1.name}: {reason1}")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    reason2 = LogarithmOfReason(agent2).calculate_reason()
    lines.append(f"{agent2.name}: {reason2}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
