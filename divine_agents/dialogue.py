from typing import List, Tuple, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_steps: Optional[List[Tuple[float, float]]] = None,
    tension_steps: Optional[List[Tuple[float, float]]] = None,
    rounds: int = 1,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First agent.
    agent2 : Agent
        Second agent.
    emotion_steps : list of tuple, optional
        Sequence of emotion updates for each round as ``(e1, e2)``.
    tension_steps : list of tuple, optional
        Sequence of tension updates for each round as ``(t1, t2)``.
    rounds : int
        Number of dialogue rounds.
    """
    lines: List[str] = []
    emotion_steps = emotion_steps or []
    tension_steps = tension_steps or []

    for i in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        if i < len(emotion_steps):
            e1, e2 = emotion_steps[i]
            agent1.update_emotion(e1)
            agent2.update_emotion(e2)
        if i < len(tension_steps):
            t1, t2 = tension_steps[i]
            agent1.update_tension(t1)
            agent2.update_tension(t2)

        # Perform transitions after applying updates
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
