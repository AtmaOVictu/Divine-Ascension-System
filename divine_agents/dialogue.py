"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def ontological_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a multi-round debate with emotional escalation.

    Agents discuss philosophical truths and may transition states when
    emotion or tension thresholds are exceeded.
    """
    history: List[str] = []
    for _ in range(rounds):
        history.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        history.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + 0.3)
        history.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.3)
        history.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return history
