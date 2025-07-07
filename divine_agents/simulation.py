from typing import List

from .agent import Agent


def dynamic_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a debate where agents may change states based on emotion.

    Parameters
    ----------
    agent1 : Agent
        First participant.
    agent2 : Agent
        Second participant.
    rounds : int, optional
        Number of exchanges to simulate, by default 3.

    Returns
    -------
    List[str]
        The lines of the conversation including transitions.
    """
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # increase emotional intensity which also raises tension
        agent1.update_emotion(agent1.emotion + 0.2)
        agent2.update_emotion(agent2.emotion + 0.2)

        prev1 = agent1.state
        prev2 = agent2.state
        new1 = agent1.transition()
        new2 = agent2.transition()

        if new1 != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")
        if new2 != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    return lines
