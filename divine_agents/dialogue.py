from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def transformation_path(agent: Agent) -> List[str]:
    """Transform the agent through all states and record dialogue."""
    lines = []
    while agent.state != "Enotnost":
        lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        agent.update_emotion(0.8)
        lines.append(f"{agent.name} prehaja v stanje: {agent.transition()}")
    lines.append(f"{agent.name} doseže stanje: {agent.state}")
    return lines
