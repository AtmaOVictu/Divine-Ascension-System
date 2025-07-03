from typing import List, Optional, Iterable, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    inc1: float = 0.8,
    inc2: float = 0.6,
    script: Optional[Iterable[Tuple[Agent, float]]] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    inc1 : float, optional
        Default emotion increment for ``agent1`` when no custom script is
        provided, by default ``0.8``.
    inc2 : float, optional
        Default emotion increment for ``agent2`` when no custom script is
        provided, by default ``0.6``.
    script : Iterable[Tuple[Agent, float]], optional
        Custom sequence of ``(agent, emotion_increment)`` pairs. When given,
        this overrides ``inc1`` and ``inc2``.
    """

    lines: List[str] = []

    # Initial responses based on current state.
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    if script is None:
        script = [(agent1, inc1), (agent2, inc2)]

    # Apply emotion updates and perform transitions according to the script.
    for ag, inc in script:
        ag.update_emotion(inc)
        lines.append(f"{ag.name} prehaja v stanje: {ag.transition()}")

    # Final responses after possible state changes.
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
