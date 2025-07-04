from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # agents experience emotions that may trigger transitions
    agent1.apply_emotion('anger')
    lines.append(f"{agent1.name} \u010cuti {agent1.emotion_label} in prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion('anger')
    lines.append(f"{agent2.name} \u010cuti {agent2.emotion_label} in prehaja v stanje: {agent2.transition()}")

    # responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
