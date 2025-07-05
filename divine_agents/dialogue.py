from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(agent1.speak())
    lines.append(agent2.speak())

    agent1.update_emotion(0.8, "anger")
    previous = agent1.history[-1]
    state = agent1.transition()
    if state != previous:
        lines.append(f"{agent1.name} prehaja v stanje: {state}")

    agent2.update_emotion(0.6, "joy")
    previous = agent2.history[-1]
    state = agent2.transition()
    if state != previous:
        lines.append(f"{agent2.name} prehaja v stanje: {state}")

    lines.append(agent1.speak())
    lines.append(agent2.speak())
    return lines
