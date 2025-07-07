"""Utility for simulating philosophical dialogue between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions rise during debate
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition(use_matrix=True)}")

    agent2.update_emotion(0.6, "empathy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition(use_matrix=True)}")

    # final statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
