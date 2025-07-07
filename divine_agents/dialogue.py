"""Utilities to simulate philosophical conversations."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation evolves as emotions rise which may trigger state
    transitions. Each response reflects the agent's current ontological and
    emotional stance.
    """

    lines: List[str] = []

    # Initial claims about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react to the opposing view increasing emotion and tension
    agent1.update_emotion(agent1.emotion + 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
