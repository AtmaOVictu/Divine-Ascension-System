from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents express their view of truth, update their emotional state and
    potentially transition to a new ontological phase.
    """
    lines: List[str] = []

    # Initial statements based on current state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions to the opposing view
    agent1.update_emotion(0.8, mood='jeza')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, mood='radovednost')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after the emotional shift
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
