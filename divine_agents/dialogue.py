from __future__ import annotations

"""Module handling philosophical dialogues between ontological agents."""

from typing import List

from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a multi-round philosophical debate between two agents.

    Each round both agents respond according to their current ontological state
    and emotion. Emotions are updated to increase tension and may trigger
    state transitions.
    """
    lines: List[str] = []

    # predefined emotional progress for demonstration
    emotions = [
        ("anger", 0.6, "calm", 0.4),
        ("curiosity", 0.2, "conviction", 0.3),
        ("acceptance", 0.5, "enlightenment", 0.5),
    ]

    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        emo1, val1, emo2, val2 = emotions[i % len(emotions)]
        agent1.update_emotion(emo1, val1)
        agent2.update_emotion(emo2, val2)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final reflections
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
