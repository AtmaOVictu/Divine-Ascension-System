from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a multilingual philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.language}): {agent1.respond('Truth?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.language}): {agent2.respond('Truth?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} transitions to: {agent1.evolve()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} transitions to: {agent2.evolve()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Truth?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Truth?')}"
    )
    return lines
