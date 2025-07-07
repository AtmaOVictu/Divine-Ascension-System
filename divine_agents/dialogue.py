from typing import List, Optional, Dict
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    turns: int = 1,
    adjustments: Optional[List[Dict[str, float]]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2: Agent
        Interacting agents.
    turns: int, optional
        Number of dialogue turns to perform. If ``adjustments`` is provided,
        its length overrides this value.
    adjustments: list of dict, optional
        Optional per-turn emotion or tension updates. Accepted keys are
        ``'a1_emotion'``, ``'a2_emotion'``, ``'a1_tension'`` and
        ``'a2_tension'``.
    """

    lines: List[str] = []

    if adjustments:
        turns = max(turns, len(adjustments))

    for i in range(turns):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        adj = adjustments[i] if adjustments and i < len(adjustments) else {}

        if "a1_emotion" in adj:
            agent1.update_emotion(adj["a1_emotion"])
        if "a2_emotion" in adj:
            agent2.update_emotion(adj["a2_emotion"])
        if "a1_tension" in adj:
            agent1.update_tension(adj["a1_tension"])
        if "a2_tension" in adj:
            agent2.update_tension(adj["a2_tension"])

        if agent1.state != agent2.state:
            agent1.update_emotion(min(agent1.emotion + 0.1, 1.0))
            agent2.update_emotion(min(agent2.emotion + 0.1, 1.0))

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
