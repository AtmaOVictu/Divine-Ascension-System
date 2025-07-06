from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak_truth()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak_truth()}")

    # Emotions rise during the discussion
    agent1.set_emotion("fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again after emotional shift
    lines.append(f"{agent1.name}: {agent1.speak_truth()}")
    lines.append(f"{agent2.name}: {agent2.speak_truth()}")

    return lines
