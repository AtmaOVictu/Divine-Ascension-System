from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    # Emotional reactions influence tension and trigger transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # Second round of responses after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('And now?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('And now?')}")
    return lines
