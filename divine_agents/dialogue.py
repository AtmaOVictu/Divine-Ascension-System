"""Dialogue helpers for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    e1_update: float = 0.8,
    e2_update: float = 0.6,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    e1_update, e2_update:
        Emotion increments applied to ``agent1`` and ``agent2``. High emotion
        levels may trigger state transitions.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(e1_update)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(e2_update)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


__all__ = ["philosophical_dialogue"]
