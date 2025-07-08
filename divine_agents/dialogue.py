from typing import List, Optional
import random
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_inc1: Optional[float] = None,
    emotion_inc2: Optional[float] = None,
    tension_inc1: Optional[float] = None,
    tension_inc2: Optional[float] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotion increments raise tension, triggering state transitions when
    thresholds are exceeded. If increments are not provided, random values
    are used to illustrate dynamic emotional shifts.
    """

    # Determine increments, randomize if not provided
    if emotion_inc1 is None:
        emotion_inc1 = random.uniform(0.5, 0.9)
    if emotion_inc2 is None:
        emotion_inc2 = random.uniform(0.5, 0.9)
    if tension_inc1 is None:
        tension_inc1 = random.uniform(0.0, 0.2)
    if tension_inc2 is None:
        tension_inc2 = random.uniform(0.0, 0.2)

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions influence tension and may cause transitions
    agent1.update_emotion(emotion_inc1)
    agent1.increase_tension(tension_inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion_inc2)
    agent2.increase_tension(tension_inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
