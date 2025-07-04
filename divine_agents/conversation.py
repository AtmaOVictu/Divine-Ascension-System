"""Utilities for simulating philosophical debates between agents."""

from typing import List

from .agent import Agent


def dynamic_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run a multi-round dialogue adjusting emotions and transitions.

    Parameters
    ----------
    agent1, agent2: :class:`Agent`
        Conversing agents.
    rounds: int, optional
        Number of conversational rounds.

    Returns
    -------
    List[str]
        Dialogue lines describing the conversation and state changes.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.2, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.2, 1.0))

        lines.append(f"{agent1.name} -> {agent1.transition()}")
        lines.append(f"{agent2.name} -> {agent2.transition()}")

    return lines


