from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    question: str = "Kaj je resnica?",
    emotions: Tuple[float, float] | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    question:
        The question both agents respond to.
    emotions:
        Optional pair of emotion adjustments applied to ``agent1`` and ``agent2``.
    """

    if emotions is None:
        emotions = (0.8, 0.6)

    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}) odgovarja na '{question}': {agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}) odgovarja na '{question}': {agent2.respond(question)}"
    )

    agent1.update_emotion(emotions[0])
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotions[1])
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")
    return lines
