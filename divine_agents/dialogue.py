"""Dialogue helpers for ontological agents."""

from typing import List
from .agent import Agent, DynamicAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    if isinstance(agent1, DynamicAgent):
        agent1_state = agent1.evolve()
    else:
        agent1_state = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1_state}")

    agent2.update_emotion(0.6)
    if isinstance(agent2, DynamicAgent):
        agent2_state = agent2.evolve()
    else:
        agent2_state = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2_state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


__all__ = [
    "philosophical_dialogue",
    "Agent",
    "DynamicAgent",
]
