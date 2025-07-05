from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    if agent1.is_legitimate_transition():
        lines.append(f"{agent1.name} legitimno prehaja v stanje: {agent1.transition()}")
    else:
        lines.append(f"{agent1.name} amatersko prehaja v stanje: {agent1.transition(force=True)}")

    agent2.update_emotion(0.6)
    if agent2.is_legitimate_transition():
        lines.append(f"{agent2.name} legitimno prehaja v stanje: {agent2.transition()}")
    else:
        lines.append(f"{agent2.name} amatersko prehaja v stanje: {agent2.transition(force=True)}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
