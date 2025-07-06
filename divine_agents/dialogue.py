from typing import Iterable, List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    sequence: Iterable[Tuple[Tuple[str, float], Tuple[str, float]]],
) -> List[str]:
    """Simulate a philosophical dialogue based on emotion sequence.

    Parameters
    ----------
    agent1, agent2:
        Agents participating in the dialogue.
    sequence:
        Iterable of emotion updates for each turn. Each element is a pair of
        ``(emotion_type, intensity)`` tuples, first for ``agent1`` then
        ``agent2``.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for emo1, emo2 in sequence:
        agent1.update_emotion(emo1[1], emo1[0])
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(emo2[1], emo2[0])
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
