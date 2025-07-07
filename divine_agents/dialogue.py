from typing import List
import random

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    return multi_round_dialogue(agent1, agent2, rounds=1)


def multi_round_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run a multi-round dialogue where emotions escalate."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions randomly and attempt transitions
        agent1.update_emotion(random.choice(list(Agent.EMOTIONS.keys())))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(random.choice(list(Agent.EMOTIONS.keys())))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
