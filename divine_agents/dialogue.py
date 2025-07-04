from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""

    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")

    # Agent1 reacts with doubt after hearing Agent2
    agent1.update_emotion("doubt")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak()}")

    # Agent2 feels joy from the discussion
    agent2.update_emotion("joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak()}")

    return lines
