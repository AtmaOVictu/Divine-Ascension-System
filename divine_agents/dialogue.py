from typing import List

from .agent import Agent
from .cluster import Cluster


def philosophical_dialogue(agent1: Agent, agent2: Agent, language: str = "en") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?', language)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?', language)}")

    lines.append(agent1.update_emotion("anger", 0.8, language))
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    lines.append(agent2.update_emotion("joy", 0.6, language))
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('What is truth?', language)}")
    lines.append(f"{agent2.name}: {agent2.respond('What is truth?', language)}")
    return lines


def collective_philosophical_dialogue(cluster: Cluster, language: str = "en") -> List[str]:
    """Simulate dialogue for a cluster of agents."""
    lines: List[str] = []
    cluster.synchronize()
    for agent in cluster.agents:
        lines.append(f"{agent.name} ({agent.state}): {agent.respond('What is truth?', language)}")
    return lines
