from typing import List
from .agent import Agent
from .cluster import Cluster


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?', 'en')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?', 'en')}")

    agent1.update_emotion('anger', 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion('joy', 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(agent1.log_transition())
    lines.append(agent2.log_transition())

    lines.append(f"{agent1.name}: {agent1.respond('What is truth?', 'en')}")
    lines.append(f"{agent2.name}: {agent2.respond('What is truth?', 'en')}")
    return lines


def collective_philosophical_dialogue(cluster: Cluster) -> List[str]:
    """Simulate a collective philosophical dialogue where emotions and tensions are shared."""
    lines = []
    for agent in cluster.agents:
        lines.append(f"{agent.name} ({agent.state}): {agent.respond('What is truth?', 'en')}")
        agent.transition()
        lines.append(f"{agent.name} transitions to: {agent.state}")
    return lines
