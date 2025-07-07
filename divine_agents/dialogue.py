from typing import List

from .agent import Agent
from .manager import ManagerAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []
    manager = ManagerAgent("dialogue-manager")
    manager.add_agent(agent1)
    manager.add_agent(agent2)

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotional states and manage transitions
    agent1.update_emotion(agent1.emotion + 0.6)
    agent2.update_emotion(agent2.emotion + 0.6)
    manager.manage_transitions()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Second round of discussion
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
