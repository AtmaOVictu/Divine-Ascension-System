from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, e1: float = 0.8, e2: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First interacting agent.
    agent2 : Agent
        Second interacting agent.
    e1 : float, optional
        Emotion intensity applied to ``agent1`` during the dialogue.
    e2 : float, optional
        Emotion intensity applied to ``agent2`` during the dialogue.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(e1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(e2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
