from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, emo1: float = 0.8, emo2: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first agent participating in the dialogue.
    agent2 : Agent
        The second agent.
    emo1 : float, optional
        Emotion increment applied to ``agent1`` during the conversation.
    emo2 : float, optional
        Emotion increment applied to ``agent2`` during the conversation.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emo1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emo2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
