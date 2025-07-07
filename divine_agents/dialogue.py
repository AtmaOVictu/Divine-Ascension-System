from typing import List

from .agent import Agent
from .manager import ManagerAgent


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


def managed_philosophical_dialogue(agent1: Agent, agent2: Agent, manager: ManagerAgent) -> List[str]:
    """Simulate a dialogue managed by a manager agent."""
    manager.add_agent(agent1)
    manager.add_agent(agent2)

    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    ]

    # Emotions influence tension and may lead to transitions
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    manager.manage_transitions()

    lines.append(f"{agent1.name} je zdaj v stanju: {agent1.state}")
    lines.append(f"{agent2.name} je zdaj v stanju: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
