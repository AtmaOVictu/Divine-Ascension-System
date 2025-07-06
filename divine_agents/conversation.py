"""Conversation utilities for philosophical agents."""
from typing import List
from .agent import Agent


def debate(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Simulate a multi-turn debate and return the conversation lines."""
    lines = []
    for _ in range(turns):
        # Agents state their understanding of truth
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotion to simulate rising tension
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
