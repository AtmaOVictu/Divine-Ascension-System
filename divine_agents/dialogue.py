from typing import List
from .agent import Agent
from .i18n import QUESTION


def philosophical_dialogue(agent1: Agent, agent2: Agent, lang1: str = "sl", lang2: str = "sl") -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Agents participating in the dialogue.
    lang1, lang2 : str, optional
        Languages for ``agent1`` and ``agent2`` responses (``"sl"`` or ``"en"``).
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(QUESTION[lang1], language=lang1)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(QUESTION[lang2], language=lang2)}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(QUESTION[lang1], language=lang1)}")
    lines.append(f"{agent2.name}: {agent2.respond(QUESTION[lang2], language=lang2)}")
    return lines
