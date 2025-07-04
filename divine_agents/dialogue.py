"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2: Agent
        Agents participating in the dialogue.
    rounds: int
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

        # Increase emotions and tension deterministically
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent1.update_tension(min(agent1.tension + 0.2, 1.0))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.2, 1.0))
        agent2.update_tension(min(agent2.tension + 0.2, 1.0))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
