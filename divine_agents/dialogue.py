"""Dialogue helpers for ontological agents."""

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


def imaginary_time_dialogue(agent1: Agent, agent2: Agent, cycles: int = 10) -> List[str]:
    """Simulate a dialogue that progresses through imaginary time cycles.

    Each cycle increases the agents' emotions, potentially triggering
    state transitions. The function returns all dialogue lines generated
    during the simulation.
    """

    history: List[str] = []
    for idx in range(1, cycles + 1):
        history.append(f"Zanka {idx}:")
        history.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        history.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotions gradually to mimic rising tension
        agent1.update_emotion(min(1.0, agent1.emotion + 0.1))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.1))

        agent1_state = agent1.transition()
        agent2_state = agent2.transition()

        history.append(f"{agent1.name} prehaja v stanje: {agent1_state}")
        history.append(f"{agent2.name} prehaja v stanje: {agent2_state}")

    return history
