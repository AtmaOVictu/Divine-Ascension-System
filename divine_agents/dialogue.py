from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue and trigger state transitions."""
    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during discussion
    agent1.update_emotion(agent1.emotion + 0.6)
    previous = agent1.history[-1]
    agent1.transition()
    if agent1.state != previous:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(agent2.emotion + 0.8)
    previous = agent2.history[-1]
    agent2.transition()
    if agent2.state != previous:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
