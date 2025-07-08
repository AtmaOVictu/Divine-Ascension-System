"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round agents respond according to their current ontological
    state, emotions intensify and may trigger state transitions.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.change_emotion(0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.change_emotion(0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
