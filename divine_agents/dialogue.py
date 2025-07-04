from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participants in the dialogue.
    rounds:
        Number of exchange rounds to simulate.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion("anger" if agent1.state == "Ego" else "joy", 0.6)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion("fear" if agent2.state == "Jaz" else "joy", 0.4)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
