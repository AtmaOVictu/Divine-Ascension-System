from typing import List
import random

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, cycles: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2: Agent
        Conversing agents.
    cycles: int
        Number of conversational cycles.
    """

    lines: List[str] = []
    for _ in range(cycles):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_tension(random.random())
        agent1.update_emotion(random.random())
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_tension(random.random())
        agent2.update_emotion(random.random())
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
