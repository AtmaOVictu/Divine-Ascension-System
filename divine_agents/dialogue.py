from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, emotion1: str | None = None, emotion2: str | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents participating in the dialogue.
    emotion1, emotion2:
        Optional emotion names applied to each agent before transitioning.
    """

    lines: List[str] = []
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    if emotion1:
        agent1.apply_emotion(emotion1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    if emotion2:
        agent2.apply_emotion(emotion2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))
    return lines
