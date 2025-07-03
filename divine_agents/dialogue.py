from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The dialogue demonstrates how emotional shifts trigger state transitions
    and alter the philosophical perspective of each agent.
    """
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions influence tension and trigger potential transitions
    agent1.update_emotion(0.8, name="jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, name="veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections from their possibly new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
