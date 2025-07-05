from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate between two agents."""

    lines: List[str] = []
    # Initial statements reflecting current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise as debate unfolds
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} meditira: {agent1.meditate()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} meditira: {agent2.meditate()}")

    # Second round after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
