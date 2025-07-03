from typing import List, Callable, Tuple, Union
from .agent import Agent


EmotionSpec = Union[Tuple[float, float], Callable[[], Tuple[float, float]]]


def _resolve_increments(spec: EmotionSpec) -> Tuple[float, float]:
    """Return a pair of emotion increments from a spec which may be a tuple or callable."""
    if callable(spec):
        return spec()
    return spec


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    increments: EmotionSpec = (0.8, 0.6),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Participants in the dialogue.
    increments : tuple or callable, optional
        Emotion increments for ``agent1`` and ``agent2``. A callable should
        return a ``(float, float)`` pair. Default increments ensure a transition
        for both agents.
    """
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    inc1, inc2 = _resolve_increments(increments)

    agent1.update_emotion(inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
