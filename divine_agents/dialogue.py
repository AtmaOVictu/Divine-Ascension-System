from typing import Iterable, List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Iterable[Tuple[str, float, str]] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    emotions:
        Optional iterable of updates ``(agent_name, intensity, emotion_name)``.
        Emotions are applied sequentially and may trigger state transitions.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    if emotions:
        for name, value, emotion_name in emotions:
            target = agent1 if name == agent1.name else agent2
            target.update_emotion(value, emotion_name)
            lines.append(
                f"{target.name} občuti {target.emotion_name} in prehaja v stanje: {target.transition()}"
            )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
