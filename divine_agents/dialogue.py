from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First debating agent.
    agent2 : Agent
        Second debating agent.
    rounds : int, optional
        How many exchanges should occur. Default is ``2``.
    """

    lines: List[str] = []
    for _ in range(rounds):
        # Each agent responds from their current ontological state
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions rise as debate continues which influences tension
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0), "anger")
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), "joy")

        # Attempt transitions if thresholds are met
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
