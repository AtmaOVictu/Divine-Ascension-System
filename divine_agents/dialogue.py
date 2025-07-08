from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    question: str,
    emo_delta1: float,
    tens_delta1: float,
    emo_delta2: float,
    tens_delta2: float,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents participating in the conversation.
    question:
        The philosophical question both agents respond to.
    emo_delta1, tens_delta1:
        Emotion and tension increments for ``agent1``.
    emo_delta2, tens_delta2:
        Emotion and tension increments for ``agent2``.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Apply emotional and tension changes for agent1
    agent1.emotion += emo_delta1
    agent1.tension += emo_delta1
    agent1.tension += tens_delta1
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Apply emotional and tension changes for agent2
    agent2.emotion += emo_delta2
    agent2.tension += emo_delta2
    agent2.tension += tens_delta2
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")
    return lines
