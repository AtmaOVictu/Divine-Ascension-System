"""Dialogue helpers for ontological agents."""
from __future__ import annotations

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2: Agent
        Participants in the conversation.
    rounds: int
        Number of interaction cycles.

    Returns
    -------
    List[str]
        Transcript of the dialogue.
    """
    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.update_emotion(0.8, "anger")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.6, "joy")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
