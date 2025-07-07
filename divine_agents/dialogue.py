from typing import List
import random

from .agent import Agent


def dialogue_round(agent1: Agent, agent2: Agent, rounds: int) -> List[str]:
    """Simulate a multi-round debate where emotions escalate."""
    dialogue_log: List[str] = []

    for _ in range(rounds):
        agent1_response = agent1.respond("Kaj je resnica?")
        agent2_response = agent2.respond("Kaj je resnica?")

        dialogue_log.append(f"{agent1.name}: {agent1_response}")
        dialogue_log.append(f"{agent2.name}: {agent2_response}")

        agent1.update_emotion("joy" if random.random() > 0.5 else "fear")
        agent1.transition()

        agent2.update_emotion("anger" if random.random() > 0.5 else "joy")
        agent2.transition()

    return dialogue_log
