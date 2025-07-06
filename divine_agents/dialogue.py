"""Utility functions for philosophical dialogues between agents."""

from __future__ import annotations

from typing import List

from .agent import Agent
from .symbolic import transition_symbol


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally and may transition
    agent1.update_emotion(0.8)
    sym1 = transition_symbol(agent1.tension, agent1.emotion)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()} {sym1}")

    agent2.update_emotion(0.6)
    sym2 = transition_symbol(agent2.tension, agent2.emotion)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()} {sym2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
