"""Dialogue utilities for philosophical discussions between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Agents adjust emotion and tension after each exchange which may trigger
    state transitions. The resulting lines show how their viewpoints evolve.
    """

    lines: List[str] = []

    # initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions rise during the debate
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final statements after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
