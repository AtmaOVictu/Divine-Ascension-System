"""Dialogue utilities for ontological agents."""

from __future__ import annotations

from typing import List

from .agent import Agent, State


def philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 2) -> List[str]:
    """Simulate a dialogue where emotions trigger possible transitions."""

    lines: List[str] = []

    for _ in range(steps):
        lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotions which in turn influence tension
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    return lines

