from typing import List

from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate where emotion triggers state changes."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Increase emotional intensity and provoke state transitions
    agent1.update_emotion(0.6, 'anger')
    agent2.update_emotion(0.8, 'joy')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kako vidiš resnico zdaj?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako vidiš resnico zdaj?')}")
    return lines
