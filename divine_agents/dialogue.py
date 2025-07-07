from typing import List
from .agent import Agent
from .sub_agent import SubAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # attach logging sub-agents
    sa1 = SubAgent(f"{agent1.name}-logger")
    sa2 = SubAgent(f"{agent2.name}-logger")
    agent1.add_sub_agent(sa1)
    agent2.add_sub_agent(sa2)

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # include sorted logs for demonstration
    lines.extend(sa1.sort_logs())
    lines.extend(sa2.sort_logs())
    return lines
