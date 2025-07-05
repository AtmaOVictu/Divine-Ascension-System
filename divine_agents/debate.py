"""Agent debate simulation module."""

from typing import List

from .agent import Agent


def debate_agents(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a debate between two agents.

    Each round both agents respond based on their current ontological
    state and emotion. Emotions escalate slightly each round which may
    trigger state transitions when thresholds are exceeded.
    """
    lines: List[str] = []
    for i in range(rounds):
        lines.append(f"Round {i + 1}:")
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))

        # record transitions if any
        prev_state1 = agent1.state
        prev_state2 = agent2.state
        agent1.transition()
        agent2.transition()
        if agent1.state != prev_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
