from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation updates each agent's emotion which may trigger a
    state transition based on defined thresholds.
    """
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during discussion
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7, "strast")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round with potentially new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
