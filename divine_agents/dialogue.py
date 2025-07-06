from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents.

    Each round both agents respond according to their current ontological
    state, then their emotions rise which may trigger state transitions.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    rounds : int, optional
        Number of conversational exchanges, by default 2.
    """

    lines: List[str] = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotion grows as debate continues
        agent1.update_emotion(0.4 + 0.1 * i)
        agent2.update_emotion(0.5 + 0.1 * i)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
