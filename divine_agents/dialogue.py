from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    During each round agents express their view on truth, update their
    emotional state which influences tension, transition if thresholds are
    met and then respond again.
    """
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(agent1.speak())
        lines.append(agent2.speak())

        agent1.update_emotion(agent1.emotion + 0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        agent2.update_emotion(agent2.emotion + 0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(agent1.speak())
        lines.append(agent2.speak())
    return lines
