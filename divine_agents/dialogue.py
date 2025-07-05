"""Utilities for simulating philosophical dialogues between agents."""
from __future__ import annotations

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a simple dialogue where agents discuss their view of truth."""
    lines: List[str] = []

    # Initial statements based on current state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional exchange influencing tension and transitions
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} čuti {agent1.emotion_type} in pravi: {agent1.respond('Kaj je resnica?')}")
    agent2.update_emotion(0.4, "mirnost")
    lines.append(f"{agent2.name} čuti {agent2.emotion_type} in odgovori: {agent2.respond('Kaj je resnica?')}")

    # Increase tension and attempt transitions
    agent1.update_tension(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
