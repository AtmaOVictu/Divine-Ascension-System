from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents participating in the conversation.
    rounds:
        Number of interaction rounds.
    """
    lines: List[str] = []

    for _ in range(rounds):
        # Each agent responds from its current state
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions rise as the discussion continues
        agent1.update_emotion(agent1.emotion + 0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
