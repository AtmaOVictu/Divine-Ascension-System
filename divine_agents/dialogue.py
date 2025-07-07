from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, *, hide_emotions: bool = False) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Agents participating in the conversation.
    hide_emotions : bool, optional
        If ``True``, emotional expressions are suppressed in responses.
    """

    agent1.hide_emotion(hide_emotions)
    agent2.hide_emotion(hide_emotions)

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional changes during debate
    agent1.set_emotion('jeza', 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion('veselje', 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
