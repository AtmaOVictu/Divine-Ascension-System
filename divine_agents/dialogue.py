from typing import List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    agent1_emotion: Optional[float] = 0.8,
    agent1_tension: Optional[float] = None,
    agent2_emotion: Optional[float] = 0.6,
    agent2_tension: Optional[float] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First conversational agent.
    agent2 : Agent
        Second conversational agent.
    agent1_emotion : float, optional
        Emotion adjustment applied to ``agent1`` before transitioning.
    agent1_tension : float, optional
        Tension level set for ``agent1`` before transitioning. If ``None`` the
        tension is left unchanged.
    agent2_emotion : float, optional
        Emotion adjustment applied to ``agent2`` before transitioning.
    agent2_tension : float, optional
        Tension level set for ``agent2`` before transitioning. If ``None`` the
        tension is left unchanged.
    """
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    if agent1_emotion is not None:
        agent1.update_emotion(agent1_emotion)
    if agent1_tension is not None:
        agent1.update_tension(agent1_tension)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    if agent2_emotion is not None:
        agent2.update_emotion(agent2_emotion)
    if agent2_tension is not None:
        agent2.update_tension(agent2_tension)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
