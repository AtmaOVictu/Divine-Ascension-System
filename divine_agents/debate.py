"""Utilities for running extended philosophical debates between agents."""
from __future__ import annotations

from typing import List

from .agent import Agent


def dynamic_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a multi-round debate between two agents.

    Each round increases the agents' emotion and tension which may trigger
    state transitions.
    """
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions
        agent1.update_emotion(agent1.emotion + 0.3, name="jeza")
        agent2.update_emotion(agent2.emotion + 0.4, name="radovednost")

        # perform transitions if thresholds are exceeded
        agent1.transition()
        agent2.transition()

    return transcript
