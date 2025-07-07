"""Conversation helpers used by the ontological agent system.

This module defines utilities for simulating philosophical discussions between
agents.  Interactions update each agent's emotional state and may trigger a
change in ontological phase based on the underlying thresholds.
"""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical exchange and update agent states.

    The dialogue showcases how agents in different ontological phases interpret
    the notion of truth.  Each participant responds according to its current
    state, then emotions are increased to demonstrate a possible transition.
    The resulting conversation is returned line by line for further processing
    or display.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
