"""Utilities for simulating philosophical conversations between agents."""

from typing import Iterable, List

from .agent import Agent


def simulate_debate(
    agent1: Agent, agent2: Agent, emotions1: Iterable[float], emotions2: Iterable[float]
) -> List[str]:
    """Run a debate updating emotions per round and collecting dialogue lines.

    Parameters
    ----------
    agent1, agent2 : Agent
        Agents participating in the debate.
    emotions1, emotions2 : Iterable[float]
        Sequences of emotional intensities applied to ``agent1`` and ``agent2``
        respectively in each round.

    Returns
    -------
    List[str]
        Dialogue lines describing the conversation and transitions.
    """

    lines: List[str] = []
    for e1, e2 in zip(emotions1, emotions2):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(e1)
        agent2.update_emotion(e2)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
