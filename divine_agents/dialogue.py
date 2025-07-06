"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Retained for backward compatibility: single round debate."""
    return philosophical_debate(agent1, agent2, rounds=1)


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a multi-round philosophical debate between two agents."""

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.set_emotion("jeza", agent1.emotion + 0.3)
        new_state1 = agent1.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

        agent2.set_emotion("veselje", agent2.emotion + 0.4)
        new_state2 = agent2.transition()
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return lines
