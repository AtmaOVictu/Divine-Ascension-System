from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical exchange and trigger transitions."""

    lines: List[str] = []

    # Initial statements
    lines.append(agent1.speak())
    lines.append(agent2.speak())

    # Emotions rise during debate
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents speak again from the new state
    lines.append(agent1.speak())
    lines.append(agent2.speak())

    return lines
