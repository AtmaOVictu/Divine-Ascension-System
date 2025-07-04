import random
from typing import List

from .agent import Agent


def debug_cycle(agent1: Agent, agent2: Agent, iterations: int = 10, seed: int | None = None) -> List[str]:
    """Run a deterministic debugging cycle with random transitions.

    Parameters
    ----------
    agent1, agent2: Agent
        Agents participating in the dialogue.
    iterations: int
        Number of interaction rounds.
    seed: int | None
        Random seed for reproducibility.

    Returns
    -------
    List[str]
        Collected dialogue lines.
    """
    rng = random.Random(seed)
    lines: List[str] = []
    for i in range(iterations):
        lines.append(f"-- Iteracija {i + 1} --")
        agent1.update_tension(rng.random())
        agent1.update_emotion(rng.random())
        agent2.update_tension(rng.random())
        agent2.update_emotion(rng.random())
        agent1.transition()
        agent2.transition()
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
