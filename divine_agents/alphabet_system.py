"""Utilities for creating and simulating alphabet-based agents."""

from __future__ import annotations

import string
from typing import List

from .agent import Agent


def create_alphabet_agents() -> List[Agent]:
    """Return a list of :class:`Agent` objects for letters A-Z."""
    return [Agent(name=char) for char in string.ascii_uppercase]


def transition_all(agents: List[Agent]) -> None:
    """Apply a transition on all agents after increasing their tension."""
    for agent in agents:
        agent.update_tension(0.8)
        agent.transition()


def alphabet_dialogue(agents: List[Agent]) -> List[str]:
    """Run a short dialogue chain through the alphabet."""
    lines: List[str] = []
    for idx in range(len(agents) - 1):
        a, b = agents[idx], agents[idx + 1]
        lines.append(f"{a.name} ({a.state}): {a.respond('Kaj je resnica?')}")
        lines.append(f"{b.name} ({b.state}): {b.respond('Kaj je resnica?')}")
        a.update_emotion(0.6, "joy")
        b.update_emotion(0.6, "anger")
        a.transition()
        b.transition()
    return lines
