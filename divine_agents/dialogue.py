"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate between two agents.

    The agents exchange views on truth. After hearing the opponent, their
    emotional intensity rises which may trigger a state transition.
    """

    lines: List[str] = []

    # Initial stances
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Both agents grow more emotional as they argue
    agent1.update_emotion(agent1.emotion + 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako zdaj vidiš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako zdaj vidiš resnico?')}")

    return lines
