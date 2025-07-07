from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical debate between two agents.

    Agents express their view of truth according to their ontological
    state and emotional tone. After each round their emotions intensify,
    which may trigger state transitions.
    """
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))

        prev1 = agent1.state
        prev2 = agent2.state
        if agent1.transition() != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.transition() != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
