from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation consists of two rounds. After each round the agents update
    their emotional state which may trigger a transition to a new ontological
    phase.
    """

    lines: List[str] = []

    # First exchange before any emotional escalation
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reaction influences tension and potential state change
    agent1.update_emotion(0.8, 'jeza')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, 'veselje')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange after emotions were applied
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
