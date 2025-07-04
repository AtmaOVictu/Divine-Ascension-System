from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Participants in the conversation.
    rounds : int
        Number of dialogue rounds to simulate.

    Returns
    -------
    List[str]
        Lines representing the conversation and state transitions.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotion to drive potential transitions
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))

        agent1.transition()
        agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
