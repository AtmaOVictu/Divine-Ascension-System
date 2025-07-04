from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round both agents express their view of truth, emotions are updated
    which may trigger state transitions.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(agent1.speak_about_truth())
        lines.append(agent2.speak_about_truth())

        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
