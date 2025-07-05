"""Utilities for simulating philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dialogue where agents evolve over several rounds.

    Parameters
    ----------
    agent1, agent2:
        The participating agents.
    rounds:
        Number of exchanges to perform.

    Returns
    -------
    List[str]
        Transcript of the conversation with state changes.
    """
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotion which in turn increases tension
        agent1.update_emotion(agent1.emotion + 0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
