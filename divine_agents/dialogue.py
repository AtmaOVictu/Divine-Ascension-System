from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    questions: Iterable[str],
    emotion_increment: float = 0.1,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        The participating agents.
    questions:
        Sequence of questions they discuss.
    emotion_increment:
        Amount of emotion added to each agent after every exchange.
    """

    lines: List[str] = []
    for q in questions:
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(q)}")
        agent1.update_emotion(min(agent1.emotion + emotion_increment, 1))
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(q)}")
        agent2.update_emotion(min(agent2.emotion + emotion_increment, 1))
        agent1.transition()
        agent2.transition()

    return lines
