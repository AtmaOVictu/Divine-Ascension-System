"""Utilities to orchestrate philosophical conversations between agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Conversing :class:`Agent` instances.
    rounds:
        Number of conversational exchanges.

    Returns
    -------
    List[str]
        A transcript of the conversation including any state changes.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + 0.4)
        new_state1 = agent1.transition()
        if agent1.history[-2] != new_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

        agent2.update_emotion(agent2.emotion + 0.4)
        new_state2 = agent2.transition()
        if agent2.history[-2] != new_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return lines
