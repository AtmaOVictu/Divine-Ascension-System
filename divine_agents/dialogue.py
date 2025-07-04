from typing import List
import random
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, seed: int | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Interacting agents.
    seed:
        Optional seed to make the random behaviour deterministic.
    """
    if seed is not None:
        random.seed(seed)

    lines: List[str] = []
    question = "Kaj je resnica?"

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    agent1.update_emotion(random.uniform(0.4, 0.9), label="anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(random.uniform(0.4, 0.9), label="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
