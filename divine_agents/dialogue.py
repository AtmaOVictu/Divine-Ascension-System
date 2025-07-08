"""Utilities for simulating philosophical dialogues between agents."""

from typing import List
from .agent import Agent


def _exchange(agent1: Agent, agent2: Agent) -> List[str]:
    """Perform a single exchange of statements between two agents."""
    return [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue with emotional growth."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.extend(_exchange(agent1, agent2))
        agent1.update_emotion(0.8, "anger")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.6, "curiosity")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.extend(_exchange(agent1, agent2))
    return lines
