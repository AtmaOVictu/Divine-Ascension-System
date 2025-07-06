"""Utilities for running multi-round philosophical debates between agents."""

from typing import List
from .agent import Agent


def debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a debate for a given number of rounds.

    Each round both agents answer the question "Kaj je resnica?", update their
    emotional state, possibly transition to a new ontological state, and the
    exchange is recorded.
    """
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotion slightly to raise tension over time
        agent1.update_emotion(0.4)
        agent2.update_emotion(0.4)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
