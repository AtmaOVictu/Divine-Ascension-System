from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical debate between two agents."""

    lines: List[str] = []

    # Initial positions on truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    # Agent1 reacts emotionally to Agent2's view
    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")

    # Agent2 is pleased with the discussion
    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    return lines
