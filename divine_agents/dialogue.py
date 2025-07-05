from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive state transitions.

    Parameters
    ----------
    agent1, agent2:
        Interacting agents.
    rounds:
        Number of conversational exchanges.
    """

    lines: List[str] = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.4 * (i + 1), label="anger" if i == 0 else "fear")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.5 * (i + 1), label="joy" if agent2.state == 'Jaz' else "sorrow")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
