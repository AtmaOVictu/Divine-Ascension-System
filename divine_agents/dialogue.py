from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First agent involved in the dialogue.
    agent2 : Agent
        Second agent.
    rounds : int, optional
        Number of exchange rounds, by default ``2``.

    Returns
    -------
    List[str]
        Transcript of the dialogue.
    """

    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # emotions rise as debate continues
        agent1.update_emotion(agent1.emotion + 0.4)
        agent2.update_emotion(agent2.emotion + 0.3)

        if agent1.transition() != agent1.history[-2]:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.transition() != agent2.history[-2]:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
