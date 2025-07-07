from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, emotion1: float = 0.8, emotion2: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participant.
    agent2 : Agent
        Second participant.
    emotion1 : float, optional
        Emotion value applied to agent1 before transition, by default 0.8.
    emotion2 : float, optional
        Emotion value applied to agent2 before transition, by default 0.6.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
