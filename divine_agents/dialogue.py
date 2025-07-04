from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    inc1: float = 0.8,
    inc2: float = 0.6,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first participant in the dialogue.
    agent2 : Agent
        The second participant in the dialogue.
    inc1 : float, optional
        Emotion increment applied to ``agent1`` before their state transition.
    inc2 : float, optional
        Emotion increment applied to ``agent2`` before their state transition.
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
