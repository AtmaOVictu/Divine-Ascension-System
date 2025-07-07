"""Dialogue helpers for interacting philosophical agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Agents start in their current states and answer a question about truth. The
    emotional intensity is then increased which may trigger state transitions.
    After transitioning, they respond again reflecting their new states.
    """

    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa sedaj?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa sedaj?')}"
    )

    return lines
