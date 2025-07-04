"""Utility helpers to orchestrate philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first participant in the debate.
    agent2 : Agent
        The second participant in the debate.
    rounds : int, optional
        Number of conversational rounds to perform.  Each round both agents
        respond, their emotional intensity increases slightly and transitions
        are attempted.
    """

    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
