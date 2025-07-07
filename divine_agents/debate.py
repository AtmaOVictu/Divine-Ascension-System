"""Utilities for simulating philosophical debates between agents."""

from typing import List

from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a debate where agents evolve through emotional interactions.

    Parameters
    ----------
    agent1, agent2 : Agent
        Participating agents.
    rounds : int, optional
        Number of dialogue rounds.
    """
    lines: List[str] = []
    emotions = ["anger", "fear", "joy"]

    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.4 + 0.2 * i, emotions[i % len(emotions)])
        agent2.update_emotion(0.5 + 0.1 * i, emotions[(i + 1) % len(emotions)])

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
