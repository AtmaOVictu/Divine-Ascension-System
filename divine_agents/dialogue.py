"""Philosophical dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Each agent updates its emotional state during the conversation, which may
    trigger a transition to a different ontological state.
    """

    lines: List[str] = []

    # Opening statements reflecting current beliefs
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts with anger to Agent2's argument
    agent1.update_emotion(0.6, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 feels joy and becomes more unified in perspective
    agent2.update_emotion(0.8, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Closing statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
