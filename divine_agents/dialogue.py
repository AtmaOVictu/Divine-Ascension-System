from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where agents influence each other."""

    lines: List[str] = []
    for _ in range(rounds):
        # Each agent answers from its current state
        lines.append(agent1.speak())
        lines.append(agent2.speak())

        # Emotions rise as debate continues
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))

        # Transition if thresholds are met and note the change
        prev1, prev2 = agent1.state, agent2.state
        agent1.transition()
        agent2.transition()
        if agent1.state != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
