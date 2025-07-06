from typing import List

from .agent import Agent


def ontological_debate(agent1: Agent, agent2: Agent, max_rounds: int = 3) -> List[str]:
    """Run an ontological debate escalating emotions until one agent reaches
    Enotnost or the maximum rounds are exhausted.

    Parameters
    ----------
    agent1 : Agent
        First debating agent.
    agent2 : Agent
        Second debating agent.
    max_rounds : int, optional
        Maximum number of dialogue rounds, by default 3.

    Returns
    -------
    List[str]
        Dialogue lines documenting the debate and state transitions.
    """
    lines: List[str] = []

    for _ in range(max_rounds):
        # Each agent states their current understanding of truth
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions escalate as the debate intensifies
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.6)

        # Apply possible state transitions and record them
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        # Stop if unity has been reached
        if agent1.state == 'Enotnost' or agent2.state == 'Enotnost':
            break

    return lines
