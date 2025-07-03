"""Utilities for simulating philosophical dialogue between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    rounds: int = 2,
    inc1: float = 0.6,
    inc2: float = 0.6,
) -> List[str]:
    """Simulate a philosophical dialogue with emotional transitions.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    rounds:
        Number of dialogue rounds. Each round may trigger transitions.
    inc1, inc2:
        Emotion increments applied to ``agent1`` and ``agent2`` per round.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(inc1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(inc2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

