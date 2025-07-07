from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, exchanges: int = 3) -> List[str]:
    """Simulate a multi-step philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First agent participating in the dialogue.
    agent2 : Agent
        Second agent participating in the dialogue.
    exchanges : int, optional
        Number of dialogue iterations to perform, by default ``3``.

    Returns
    -------
    List[str]
        Lines representing the conversation and state transitions.
    """

    lines: List[str] = []

    for _ in range(exchanges):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(1.0, agent2.emotion + 0.2))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
