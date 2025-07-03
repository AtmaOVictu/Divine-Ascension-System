"""Utilities for multi-turn debates between ontological agents."""
from __future__ import annotations

from typing import List
import random

from .agent import Agent


def debate(agent1: Agent, agent2: Agent, rounds: int = 3, seed: int | None = None) -> List[str]:
    """Run a multi-turn philosophical debate between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Agents participating in the debate.
    rounds : int, optional
        Number of dialogue rounds to perform. Default is 3.
    seed : int | None, optional
        Seed for deterministic behaviour in tests.

    Returns
    -------
    List[str]
        The dialogue lines generated during the debate.
    """
    if seed is not None:
        random.seed(seed)

    transcript: List[str] = []
    for _ in range(rounds):
        # Each agent states their view on truth according to their state
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions escalate as discussion continues
        agent1.update_emotion(random.uniform(0.4, 0.8))
        agent2.update_emotion(random.uniform(0.4, 0.8))

        # Perform state transitions if thresholds are crossed
        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        transcript.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        transcript.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return transcript
