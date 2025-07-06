from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first participating agent.
    agent2 : Agent
        The second participating agent.
    rounds : int, optional
        Number of conversational rounds to run.
    """

    lines: List[str] = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        if i == 0:
            agent1.adjust_emotion(0.8)
            agent2.adjust_emotion(0.6)
        else:
            agent1.adjust_emotion(0.3)
            agent2.adjust_emotion(0.3)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
