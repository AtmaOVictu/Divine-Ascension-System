from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, inc1: float, inc2: float
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First conversational agent.
    agent2 : Agent
        Second conversational agent.
    inc1 : float
        Emotion increment applied to ``agent1`` during the dialogue.
    inc2 : float
        Emotion increment applied to ``agent2`` during the dialogue.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
