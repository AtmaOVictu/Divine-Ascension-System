from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short dialogue reflecting emotional transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional shift and possible transition for agent1
    agent1.update_tension(0.8)
    agent1.set_emotion(0.4, "strah")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Emotional shift and possible transition for agent2
    agent2.set_emotion(0.7, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of answers after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
