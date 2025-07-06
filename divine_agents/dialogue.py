"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents.

    Each turn increases the agents' emotional intensity which may lead to
    state transitions based on the defined thresholds.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    turns:
        Number of conversational turns to simulate.

    Returns
    -------
    List[str]
        A transcript of the dialogue lines.
    """

    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    for step in range(turns):
        # emotions escalate with each turn
        agent1.update_emotion(agent1.emotion + 0.3)
        agent2.update_emotion(agent2.emotion + 0.3)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

    return lines
