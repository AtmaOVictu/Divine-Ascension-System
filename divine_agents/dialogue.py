"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue for a given number of turns."""
    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # emotions rise slightly each turn
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))

        # perform transitions based on updated values
        agent1_state = agent1.transition()
        agent2_state = agent2.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {agent1_state}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2_state}")
    return lines
