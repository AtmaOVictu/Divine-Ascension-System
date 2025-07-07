"""Utility for simulating philosophical dialogues between agents."""
from __future__ import annotations

from typing import List

from .agent import Agent
from .manager import ManagerAgent, SubAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines


def managed_dialogue(manager: ManagerAgent, agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue managed by a ManagerAgent with helper SubAgents."""
    s1 = SubAgent(f"helper-{agent1.name}", associated_agent=agent1)
    s2 = SubAgent(f"helper-{agent2.name}", associated_agent=agent2)
    agent1.add_sub_agent(s1)
    agent2.add_sub_agent(s2)

    manager.add_agent(agent1)
    manager.add_agent(agent2)
    manager.manage_transitions()

    lines = philosophical_dialogue(agent1, agent2)
    lines.extend(s1.sort_logs())
    lines.extend(s2.sort_logs())
    return lines
