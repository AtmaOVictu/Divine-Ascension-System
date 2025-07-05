"""Dialogue helpers for ontological agents."""

from __future__ import annotations

from typing import List

from .agent import Agent, Debate


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a short dialogue demonstrating state changes."""

    debate = Debate(agent1, agent2)
    lines = []

    # Initial responses
    a1_resp, a2_resp = debate.step()
    lines.append(a1_resp)
    lines.append(a2_resp)

    # Agents experience emotions influencing tension
    agent1.feel(fear=0.8)
    agent2.feel(joy=0.6)

    # Next round after emotions updated
    a1_resp, a2_resp = debate.step()
    lines.append(a1_resp)
    lines.append(a2_resp)

    return lines

