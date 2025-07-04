import random
from typing import List
from .agent import Agent


def continuous_cycle(agent1: Agent, agent2: Agent, iterations: int = 10) -> List[str]:
    """Run random transitions for a number of iterations and collect dialogue lines."""
    lines: List[str] = []
    for i in range(iterations):
        lines.append(f"-- Iteration {i + 1} --")
        agent1.update_emotion(random.random())
        agent2.update_emotion(random.random())
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
