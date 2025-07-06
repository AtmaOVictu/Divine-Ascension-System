from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First debating agent.
    agent2 : Agent
        Second debating agent.
    steps : int, optional
        Number of conversational exchanges, by default 2.
    """
    lines: List[str] = []

    for _ in range(steps):
        # Each agent answers from its current ontological perspective
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions rise as debate continues, influencing tension
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
