from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    a1_emotion: float = 0.8,
    a2_emotion: float = 0.6,
    tension_threshold: float = 0.7,
    emotion_threshold: float = 0.5,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    a1_emotion, a2_emotion:
        Emotion updates applied before each agent transitions.
    tension_threshold, emotion_threshold:
        Thresholds forwarded to :py:meth:`Agent.transition`.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition(emotion=a1_emotion, tension_threshold=tension_threshold, emotion_threshold=emotion_threshold)}"
    )

    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition(emotion=a2_emotion, tension_threshold=tension_threshold, emotion_threshold=emotion_threshold)}"
    )

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
