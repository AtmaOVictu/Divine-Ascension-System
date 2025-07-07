from __future__ import annotations

import random
from typing import List

from .agent import Agent


class Cluster:
    """Group of agents that synchronize their state transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> None:
        """Update emotions and tensions randomly, then transition agents."""
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            agent.transition()

    def dialogue(self) -> List[str]:
        """Return combined dialogue lines for all agents in sequence."""
        lines: List[str] = []
        for i in range(len(self.agents) - 1):
            a1 = self.agents[i]
            a2 = self.agents[i + 1]
            lines.extend(philosophical_dialogue(a1, a2))
        return lines


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Generate a short dialogue reflecting agent states and emotions."""
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    agent1.update_emotion(0.6)
    agent2.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
