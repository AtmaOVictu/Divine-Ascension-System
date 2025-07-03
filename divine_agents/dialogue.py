"""Dialogue utilities for ontological agents."""
from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents over several rounds."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotion slightly to simulate engagement
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))

        prev_state1 = agent1.state
        prev_state2 = agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    return lines
