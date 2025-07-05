from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Participants in the dialogue.
    rounds : int, optional
        Number of conversational rounds to simulate.
    """

    lines: List[str] = []

    for r in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # emotions intensify as discussion continues
        agent1.update_emotion(0.6, "jeza" if r == 0 else "radovednost")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.6 if r == 0 else 0.4, "veselje" if r == 0 else "mirnost")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
