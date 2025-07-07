from typing import List
import random
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion('joy')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion('anger')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def multi_round_dialogue(agent1: Agent, agent2: Agent, rounds: int, seed: int | None = None) -> List[str]:
    """Run a multi-round dialogue where emotions escalate and states may change."""
    if seed is not None:
        random.seed(seed)
    log: List[str] = []
    for _ in range(rounds):
        log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        agent1.update_emotion(random.choice(list(Agent.EMOTIONS.keys())))
        agent1.transition()
        agent2.update_emotion(random.choice(list(Agent.EMOTIONS.keys())))
        agent2.transition()
    return log
