from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial viewpoints
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during discussion
    agent1.update_emotion(0.8, "jeza")
    lines.append(f"{agent1.name} čuti jeza in prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "sočutje")
    lines.append(f"{agent2.name} čuti sočutje in prehaja v stanje: {agent2.transition()}")

    # Updated viewpoints after emotional shift
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
