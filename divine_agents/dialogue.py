"""Utilities for generating philosophical conversations between agents."""

from typing import List

from .agent import Agent


def _increase_emotion(agent: Agent, delta: float) -> None:
    """Increase an agent's emotion level and adjust tension."""

    agent.update_emotion(min(1.0, agent.emotion + delta))


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Generate a multi-turn dialogue where emotions and states evolve.

    Each turn both agents answer the same question about truth. After every
    answer their emotional intensity rises, potentially causing state
    transitions. The resulting lines capture the response and any transition.
    """

    lines: List[str] = []
    agents = [agent1, agent2]

    for _ in range(turns):
        for ag in agents:
            lines.append(
                f"{ag.name} ({ag.state}, e={ag.emotion:.2f}): "
                f"{ag.respond('Kaj je resnica?')}"
            )
            _increase_emotion(ag, 0.3)
            lines.append(f"{ag.name} prehaja v stanje: {ag.transition()}")

    return lines

