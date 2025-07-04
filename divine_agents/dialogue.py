from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Emotions increase with every round which may trigger state transitions.
    """
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

        # escalate emotions to drive potential transitions
        agent1.update_emotion(agent1.emotion + 0.3)
        agent2.update_emotion(agent2.emotion + 0.3)

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return lines

